from datetime import date
from os import PathLike
from typing import Any, Literal

from pydantic import BaseModel, constr, root_validator, validator
from pydantic_xml import BaseXmlModel, XmlEncoder, attr, element, wrapped

from ..utils.regexes import RegexPatterns
from . import enums

NSMAP = {"": "http://www.interactivebrokers.com/schemas/IBCust_import"}


class CustomXmlEncoder(XmlEncoder):
    def encode(self, obj: Any) -> str:
        if isinstance(obj, bool):
            return str(obj).lower()

        return super().encode(obj)


class Name(BaseXmlModel, nsmap=NSMAP):
    first: constr(max_length=18) = attr()
    last: constr(max_length=50) = attr()
    middle: constr(max_length=18) | None = attr()
    salutation: constr(regex=RegexPatterns.salutation) | None = attr()


class Email(BaseXmlModel, nsmap=NSMAP):
    email: constr(regex=RegexPatterns.email) = attr()


class Phone(BaseXmlModel, nsmap=NSMAP):
    type: enums.PhoneTypeEnum = attr()
    number: constr(max_length=18) = attr()
    country: constr(min_length=3, max_length=3)

    class Config:
        arbitrary_types_allowed = True


class Residence(BaseXmlModel, nsmap=NSMAP):
    country: constr(min_length=3, max_length=3) = attr()
    state: str = attr()
    city: constr(max_length=100) = attr()
    postal_code: constr(max_length=20) = attr()
    street_1: constr(max_length=200) = attr()
    street_2: constr(max_length=200) | None = attr()


class MailingAddress(BaseXmlModel, nsmap=NSMAP):
    country: constr(min_length=3, max_length=3) = attr()
    state: str = attr()
    city: constr(max_length=100) = attr()
    postal_code: constr(max_length=20) = attr()
    street_1: constr(max_length=200) = attr()
    street_2: constr(max_length=200) | None = attr()


class Identification(BaseXmlModel, nsmap=NSMAP):
    citizenship: constr(min_length=3, max_length=3) = attr()
    issuing_country: constr(min_length=3, max_length=3) = attr(name="IssuingCountry")

    # types of ID, need to fill at least one of these
    national_card: str | None = attr(name="NationalCard")
    drivers_license: str | None = attr(name="DriversLicense")

    @root_validator
    def check_identification(cls, values):
        id1, id2 = values.get("national_card"), values.get("drivers_license")

        if not id1 and not id2:
            raise ValueError("Need to have at least one identification item")

        return values


class TaxResidency(BaseXmlModel, nsmap=NSMAP):
    country: constr(min_length=3, max_length=3) = attr()
    tin_type: enums.TINTypeEnum = attr(name="TINType")

    # Required for non-US residents who has a Foreign Tax ID
    tin: str | None = attr(name="TIN")

    class Config:
        arbitrary_types_allowed = True


class EmployerAddress(BaseXmlModel, nsmap=NSMAP):
    country: str = attr()
    state: str | None = attr()
    city: constr(max_length=100) | None = attr()
    postal_code: constr(max_length=20) | None = attr()
    street_1: constr(max_length=20) | None = attr()


class EmploymentDetails(BaseXmlModel, nsmap=NSMAP):
    employer: constr(max_length=128) = element()
    occupation: str | None = element()
    employer_business: str | None = element()
    employer_address: EmployerAddress = element()


class W8Ben(BaseXmlModel, nsmap=NSMAP):
    # whether the applicant accepts the terms (https://www.ibkrguides.com/dameca/Schema/W8Ben.htm#:~:text=Under%20penalties%20of,8BEN%20is%20correct.)
    cert: bool = attr()

    part_2_9a_country: constr(min_length=3, max_length=3) = attr()
    name: str = attr()
    blank_form: bool = attr()
    signature_type: Literal["Electronic"] | None = attr()
    tax_form_file: str = attr()
    foreign_tax_id: str | None = attr()
    proprietary_form_number: str | None = attr()
    explanation: enums.W8BenExplanationEnum | None = attr()

    class Config:
        arbitrary_types_allowed = True


class AccountHolderDetails(BaseXmlModel, nsmap=NSMAP):
    # attributes
    external_id: str = attr()
    same_mail_address: bool = attr()

    # children
    name: Name = element(tag="Name")
    country_of_birth: constr(min_length=3, max_length=3) = element(tag="CountryOfBirth")
    dob: date = element(tag="DOB")
    email: Email = element(tag="Email")
    num_dependents: int | None = element(tag="NumDependents")
    marital_status: enums.MaritalStatusEnum | None = element(tag="MaritalStatus")
    phone: list[Phone] | None = wrapped("Phones", element(tag="Phone"))
    residence: Residence = element(tag="Residence")
    mailing_address: MailingAddress | None = element(tag="MailingAddress")
    identification: Identification | None = element(tag="Identification")
    tax_residencies: list[TaxResidency] = wrapped(
        "TaxResidencies",
        element(tag="TaxResidency"),
    )
    w8ben: W8Ben | None = element(tag="W8Ben")
    employment_type: enums.EmploymentTypeEnum = element(tag="EmploymentType")
    employment_details: EmploymentDetails = element(tag="EmploymentDetails")

    class Config:
        arbitrary_types_allowed = True


class SourceOfWealth(BaseXmlModel, nsmap=NSMAP):
    percentage: int = attr()
    source_type: str = attr()
    is_used_for_funds: bool = attr()


class FinancialInformation(BaseXmlModel, nsmap=NSMAP):
    sources_of_wealth: list[SourceOfWealth] = wrapped(
        "SourcesOfWealth",
        element(tag="SourceOfWealth"),
    )


class AccountHolder(BaseXmlModel, nsmap=NSMAP):
    details: AccountHolderDetails = element(tag="AccountHolderDetails")
    financial_information: FinancialInformation = element(tag="FinancialInformation")


class Customer(BaseXmlModel, nsmap=NSMAP):
    # attributes
    email: str = attr()
    external_id: str = attr()
    has_direct_trading_access: bool = attr()
    legal_residence_country: str | None = attr()
    md_status_nonpro: bool = attr()
    meets_aml_standard: bool = attr()
    prefix: str = attr()
    customer_type: str = attr(name="type")

    # children
    account_holder: AccountHolder = element(tag="AccountHolder")


class TradingPermission(BaseXmlModel, nsmap=NSMAP):
    exchange_group: str | None = attr()
    product: str | None = attr()
    country: str | None = attr()


class Account(BaseXmlModel, nsmap=NSMAP):
    # attributes
    external_id: str = attr()
    base_currency: str = attr()
    margin: enums.AccountMarginEnum = attr()
    multicurrency: bool = attr()
    drip: bool | None = attr()
    client_active_trading: bool | None = attr()

    # children
    trading_permissions: list[TradingPermission] = wrapped(
        "TradingPermissions",
        element(tag="TradingPermission"),
    )

    class Config:
        arbitrary_types_allowed = True


class User(BaseXmlModel, nsmap=NSMAP):
    external_individual_id: str = attr()
    external_user_id: str = attr()
    prefix: constr(regex=RegexPatterns.prefix) = attr()


class AttachedFile(BaseXmlModel, nsmap=NSMAP):
    file_name: str = attr()
    file_length: str = attr()
    sha1_checksum: str = attr()

    @validator("file_name")
    def validate_file_types(cls, value):
        allowed_types = (".jpeg", ".jpg", ".pdf", ".png")

        if not value.endswith(allowed_types):
            raise ValueError("File type is invalid")

        return value


class Document(BaseXmlModel, nsmap=NSMAP):
    # attributes
    form_no: int = attr()
    exec_ts: int = attr()
    exec_login_ts: int = attr()
    proof_of_identity_type: str | None = attr()
    proof_of_address_type: str | None = attr()
    valid_address: bool | None = attr()
    expiration_date: date | None = attr()

    # children
    signed_by: str = element(tag="SignedBy")
    attached_file: AttachedFile = element(tag="AttachedFile")


class Application(BaseXmlModel, nsmap=NSMAP):
    customer: Customer = element(tag="Customer", default={})
    accounts: list[Account] = wrapped(
        "Accounts",
        element(
            tag="Account",
            default_factory=list,
        ),
    )
    users: list[User] = wrapped(
        "Users",
        element(
            tag="User",
            default_factory=list,
        ),
    )
    documents: list[Document] = wrapped(
        "Documents",
        element(
            tag="Document",
            default_factory=list,
        ),
    )


class Applications(BaseXmlModel, nsmap=NSMAP):
    applications: list[Application] = element(tag="Application", default_factory=list)


class DAMApplicationPayload(BaseModel):
    user_id: int | str

    # name information
    first_name: str
    middle_name: str | None
    last_name: str
    salutation: str | None

    # user data
    date_of_birth: date
    country_of_birth: str

    # contact data
    email: str

    # identification
    identification_citizenship: str
    identification_issuing_country: str
    identification_number: str | int

    # residence information
    country: str
    state: str
    postal_code: str
    city: str
    street_name: str
    is_mailing_address: bool = True

    # mailing address (only required if `is_mailing_address` is False)
    mailing_country: str | None
    mailing_state: str | None
    mailing_postal_code: str | None
    mailing_city: str | None
    mailing_street_name: str | None

    # employment
    employment_type: enums.EmploymentTypeEnum

    # employment details, fill if `employment_type` is EMPLOYED or SELFEMPLOYED
    employer: str | None
    occupation: str | None
    employer_business: str | None
    employer_address_country: str | None
    employer_address_state: str | None
    employer_address_city: str | None
    employer_address_postal_code: str | None
    employer_address_street_name: str | None

    # tax info
    tax_country: str
    tin: str

    # source of the wealth
    sow_type: enums.SourceOfWealthEnum

    # documents
    signed_by_name: str
    w8ben_file: str | PathLike
    proof_of_identity_file: str | PathLike
    proof_of_address_file: str | PathLike
    proof_of_address_type: enums.ProofOfAddressTypeEnum

    class Config:
        arbitrary_types_allowed = True
