import tempfile
from base64 import b64encode
from datetime import datetime
from os import PathLike
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from .brokerage import enums, models
from .brokerage.vars import DAMSettings
from .logger import logger
from .pgp import PGPHelper
from .utils import deep_get, get_file_sha1, get_file_size


class DAM:
    @classmethod
    def __generate_application_xml(cls, data: models.DAMApplicationPayload):
        current_timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        mailing_address = None
        employment_details = None

        w8ben_file = (
            Path(data.w8ben_file)
            if isinstance(data.w8ben_file, str)
            else data.w8ben_file
        )
        proof_of_identity_file = (
            Path(data.proof_of_identity_file)
            if isinstance(data.proof_of_identity_file, str)
            else data.proof_of_identity_file
        )
        proof_of_address_file = (
            Path(data.proof_of_address_file)
            if isinstance(data.proof_of_address_file, str)
            else data.proof_of_address_file
        )

        email = models.Email(email=data.email)
        name = models.Name(
            first=data.first_name,
            last=data.last_name,
            middle=data.middle_name,
        )
        identification = models.Identification(
            citizenship=data.identification_citizenship,
            issuing_country=data.identification_issuing_country,
            national_card=data.identification_number,
        )
        residence = models.Residence(
            country=data.country,
            state=data.state,
            city=data.city,
            postal_code=data.postal_code,
            street_1=data.street_name,
        )

        if not data.is_mailing_address:
            mailing_address = models.MailingAddress(
                country=data.mailing_country,
                state=data.mailing_state,
                city=data.mailing_city,
                postal_code=data.mailing_postal_code,
                street_1=data.mailing_street_name,
            )

        if data.employment_type in [
            enums.EmploymentTypeEnum.EMPLOYED,
            enums.EmploymentTypeEnum.SELFEMPLOYED,
        ]:
            employment_details = models.EmploymentDetails(
                employer=data.employer,
                occupation=data.occupation,
                employer_business=data.employer_business,
                employer_address=models.EmployerAddress(
                    country=data.employer_address_country,
                    state=data.employer_address_state,
                    city=data.employer_address_city,
                    postal_code=data.employer_address_postal_code,
                    street_1=data.employer_address_street_name,
                ),
            )

        tax_residency = models.TaxResidency(
            country=data.tax_country,
            tin_type=enums.TINTypeEnum.NON_US.value,
            tin=data.tin,
        )
        financial_information = models.FinancialInformation(
            sources_of_wealth=[
                models.SourceOfWealth(
                    percentage=100,
                    source_type=data.sow_type.value,
                    is_used_for_funds=True,
                )
            ]
        )
        w8ben = models.W8Ben(
            cert=True,
            part_2_9a_country="N/A",
            name=data.signed_by_name,
            signature_type="Electronic",
            blank_form=True,
            tax_form_file="Form5001.pdf",
            foreign_tax_id=data.tin,
        )

        account_holder = models.AccountHolder(
            details=models.AccountHolderDetails(
                external_id=data.user_id,
                same_mail_address=data.is_mailing_address,
                name=name,
                country_of_birth=data.country_of_birth,
                dob=data.date_of_birth,
                email=email,
                residence=residence,
                mailing_address=mailing_address,
                identification=identification,
                tax_residencies=[tax_residency],
                w8ben=w8ben,
                employment_type=data.employment_type,
                employment_details=employment_details,
            ),
            financial_information=financial_information,
        )

        # main models
        customer = models.Customer(
            email=data.email,
            external_id=data.user_id,
            prefix="lora",
            customer_type="INDIVIDUAL",
            md_status_nonpro=False,
            meets_aml_standard=True,
            has_direct_trading_access=False,
            account_holder=account_holder,
        )

        account = models.Account(
            external_id=data.user_id,
            base_currency="USD",
            margin=enums.AccountMarginEnum.CASH.value,
            multicurrency=False,
            drip=False,
            client_active_trading=False,
            trading_permissions=[
                models.TradingPermission(product="STOCKS", country="UNITED STATES"),
                models.TradingPermission(product="FOREX", country="HONG KONG"),
            ],
        )
        user = models.User(
            external_individual_id=data.user_id,
            external_user_id=data.user_id,
            prefix="lora",
        )
        w8ben_document = models.Document(
            form_no="5001",
            exec_ts=current_timestamp,
            exec_login_ts=current_timestamp,
            signed_by=data.signed_by_name,
            attached_file=models.AttachedFile(
                file_name=w8ben_file.name,
                file_length=get_file_size(w8ben_file),
                sha1_checksum=get_file_sha1(w8ben_file),
            ),
        )
        proof_of_identity_document = models.Document(
            form_no="8001",
            exec_ts=current_timestamp,
            exec_login_ts=current_timestamp,
            proof_of_identity_type="National ID Card",
            signed_by=data.signed_by_name,
            attached_file=models.AttachedFile(
                file_name=proof_of_identity_file.name,
                file_length=get_file_size(proof_of_identity_file),
                sha1_checksum=get_file_sha1(proof_of_identity_file),
            ),
        )
        proof_of_address_document = models.Document(
            form_no="8002",
            exec_ts=current_timestamp,
            exec_login_ts=current_timestamp,
            proof_of_address_type=data.proof_of_address_type.value,
            signed_by=data.signed_by_name,
            attached_file=models.AttachedFile(
                file_name=proof_of_address_file.name,
                file_length=get_file_size(proof_of_address_file),
                sha1_checksum=get_file_sha1(proof_of_address_file),
            ),
        )

        application = models.Application(
            customer=customer,
            accounts=[account],
            users=[user],
            documents=[
                w8ben_document,
                proof_of_identity_document,
                proof_of_address_document,
            ],
        )

        applications = models.Applications(applications=[application])

        return applications.to_xml(
            encoder=models.CustomXmlEncoder(),
            pretty_print=True,
            encoding="UTF-8",
            skip_empty=True,
            standalone=True,
        ).decode()

    @classmethod
    def __process_xml_file(cls, xml_data: str, path: Path, file_name="application.xml"):
        xml_file = path.joinpath("application.xml")

        with open(xml_file, "w") as f:
            f.write(xml_data)

        return xml_file

    @classmethod
    def __process_zip_file(cls, files: str, path: Path, file_name="data.zip"):
        zip_file = path.joinpath(file_name)

        with ZipFile(zip_file, "w", ZIP_DEFLATED) as zf:
            for file in files:
                file = Path(file) if isinstance(file, str) else file
                zf.write(file, file.name)

        return zip_file

    @classmethod
    def __encrypt_zip_file(
        cls,
        zip_file: Path,
        path: Path,
        pgp_helper: PGPHelper | None = None,
        file_name="encrypted_data.zip",
    ):
        if pgp_helper is None:
            raise ValueError("Please provide PGPHelper instance")

        encrypted_zip_file = path.joinpath(file_name)
        pgp_helper.encrypt_zip(zip_file, output=encrypted_zip_file)

        return encrypted_zip_file

    @classmethod
    def __encode_zip_file(cls, zip_file: Path):
        try:
            with open(zip_file, "rb") as f:
                file_data = f.read()

                # encode the data to base64
                encoded_data = b64encode(file_data)

                return encoded_data.decode("utf-8").replace("\n", "")
        except Exception as e:
            logger.error(f"Cannot encode zip file: {e}")

    @classmethod
    def __process_payload_file(
        cls,
        pgp_helper: PGPHelper,
        xml_data: str,
        attached_files: list[Path | PathLike | str],
        xml_file_name="application.xml",
        zip_file_name="data.zip",
    ):
        with tempfile.TemporaryDirectory() as tmp_dir:
            tmp_path = Path(tmp_dir)

            # write xml_data to file
            xml_file = cls.__process_xml_file(
                xml_data,
                path=tmp_path,
                file_name=xml_file_name,
            )

            # add the xml to the list of files
            attached_files.append(xml_file)

            # build the zip file
            zip_file = cls.__process_zip_file(
                attached_files,
                path=tmp_path,
                file_name=zip_file_name,
            )

            # encrypt zip file
            encrypted_zip_file = cls.__encrypt_zip_file(
                zip_file,
                path=tmp_path,
                pgp_helper=pgp_helper,
                file_name=f"encrypted_{zip_file_name}",
            )

            # encode it to base64
            encoded_zip_file = cls.__encode_zip_file(encrypted_zip_file)

            return encoded_zip_file

    @classmethod
    def generate_application_payload(
        cls,
        data: models.DAMApplicationPayload,
        pgp_helper: PGPHelper,
    ):
        xml_data = cls.__generate_application_xml(data)
        encoded_file_payload = cls.__process_payload_file(
            pgp_helper=pgp_helper,
            xml_data=xml_data,
            attached_files=[
                data.w8ben_file,
                data.proof_of_identity_file,
                data.proof_of_address_file,
            ],
        )

        dam_settings = DAMSettings()

        if dam_settings.not_set:
            logger.error("DAM_CSID environment variables not set, setting it to None")

        return dict(CSID=dam_settings.DAM_CSID, payload=encoded_file_payload)

    @classmethod
    def generate_account_opening_payload(cls, user_id: int, data: dict):
        contact_info = data.get("contact")
        identity_info = data.get("identity")
        disclosures_info = data.get("disclosures")

        company_information = deep_get(disclosures_info, ["context", 0], default={})

        name = models.Name(
            first=identity_info.get("given_name"),
            last=identity_info.get("family_name"),
            middle=identity_info.get("middle_name"),
        )

        residence = models.Residence(
            city=contact_info.get("city"),
            country=contact_info.get("country"),
            postal_code=contact_info.get("postal_code"),
            state=contact_info.get("state"),
            street_1=contact_info.get("street_address"),
        )

        employment_details = models.EmploymentDetails(
            employer=company_information.get("company_name"),
            employer_address=models.EmployerAddress(
                country=company_information.get("company_country")
            ),
        )

        tax_residency = models.TaxResidency(
            country=identity_info.get("country_of_tax_residence"),
            tin_type="NonUS_NationalId",
        )

        financial_information = models.FinancialInformation(
            sources_of_wealth=[
                models.SourceOfWealth(
                    percentage=100,
                    source_type="SOW_IND-Income",
                    is_used_for_funds=True,
                )
            ]
        )

        account = models.Account(
            base_currency="USD",
            external_id=user_id,
            margin="Margin",
            multicurrency=False,
            trading_permissions=[models.TradingPermission(exchange_group="US-Sec")],
        )

        user = models.User(
            external_individual_id=user_id,
            external_user_id=user_id,
            prefix="lora",
        )

        account_holder_details = models.AccountHolderDetails(
            external_id=user_id,
            same_mail_address=True,
            name=name,
            email=models.Email(email=contact_info.get("email_address")),
            country_of_birth=identity_info.get("country_of_birth"),
            dob=identity_info.get("date_of_birth"),
            residence=residence,
            identification=None,
            employment_type=disclosures_info.get("employment_status").upper(),
            employment_details=employment_details,
            title="Account Holder",
            tax_residencies=[tax_residency],
            w8ben=None,
        )

        account_holder = models.AccountHolder(
            details=account_holder_details,
            financial_information=financial_information,
        )

        customer = models.Customer(
            email=contact_info.get("email_address"),
            external_id=user_id,
            has_direct_trading_access=True,
            legal_residence_country=identity_info.get("country_of_residentship"),
            md_status_nonpro=True,
            meets_aml_standard=True,
            prefix="lora",
            customer_type="INDIVIDUAL",
            account_holder=account_holder,
        )

        application = models.Application(
            customer=customer,
            accounts=[account],
            users=[user],
            documents=[],
        )

        applications = models.Applications(applications=[application])

        return applications.to_xml(
            encoder=models.CustomXmlEncoder(),
            pretty_print=True,
            encoding="UTF-8",
            skip_empty=True,
            standalone=True,
        ).decode()
