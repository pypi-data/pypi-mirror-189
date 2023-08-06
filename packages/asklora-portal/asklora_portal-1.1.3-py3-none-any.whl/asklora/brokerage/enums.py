from enum import Enum, EnumMeta


class MetaEnum(EnumMeta):
    def __contains__(cls, item):
        try:
            cls(item)
        except ValueError:
            return False
        return True


class BaseEnum(Enum, metaclass=MetaEnum):
    pass


class ExtendedEnum(BaseEnum):
    @classmethod
    @property
    def choices(cls):
        return tuple(map(lambda c: (c.name, c.value), cls))

    @classmethod
    def to_dict(cls):
        data = {}
        for c in cls:
            data[c.name] = c.value
        return data

    @classmethod
    def to_list(cls):
        return [c.value for c in cls]

    @classmethod
    def equal(cls, value1, value2):
        if isinstance(value1, cls):
            value1 = value1.value
        if isinstance(value2, cls):
            value2 = value2.value
        return value1 == value2

    @classmethod
    def lower(cls, value):
        if isinstance(value, cls):
            value = value.value
        return value.lower()


# +++++++++++++++++++++++++++++ ENUMS START BELOW +++++++++++++++++++++++++++++


class PhoneTypeEnum(ExtendedEnum):
    WORK = "Work"
    HOME = "Home"
    FAX = "Fax"
    MOBILE = "Mobile"
    BUSINESS = "Business"


class MaritalStatusEnum(ExtendedEnum):
    SINGLE = "S"
    MARRIED = "M"
    WIDOWED = "W"
    DIVORCED = "D"
    COMMON_LAW_PARTNER = "C"


class AccountMarginEnum(ExtendedEnum):
    CASH = "Cash"
    MARGIN = "Margin"
    REGT = "RegT"
    PORTFOLIOMARGIN = "PortfolioMargin"


class TINTypeEnum(ExtendedEnum):
    US = "SSN"
    NON_US = "NonUS_NationalId"
    ORG = "EIN"


class W8BenExplanationEnum(ExtendedEnum):
    US_TIN = "US_TIN"
    TIN_NOT_DISCLOSED = "TIN_NOT_DISCLOSED"
    TIN_NOT_REQUIRED = "TIN_NOT_REQUIRED"
    TIN_NOT_ISSUED = "TIN_NOT_ISSUED"


class EmploymentTypeEnum(ExtendedEnum):
    UNEMPLOYED = "UNEMPLOYED"
    EMPLOYED = "EMPLOYED"
    SELFEMPLOYED = "SELFEMPLOYED"
    RETIRED = "RETIRED"
    STUDENT = "STUDENT"
    ATHOMETRADER = "ATHOMETRADER"
    HOMEMAKER = "HOMEMAKER"


class SourceOfWealthEnum(ExtendedEnum):
    ALLOWANCE = "SOW-IND-Allowance"
    DISABILITY = "SOW-IND-Disability"
    INCOME = "SOW-IND-Income"
    INHERITANCE = "SOW-IND-Inheritance"
    INTEREST = "SOW-IND-Interest"
    MARKETPROFIT = "SOW-IND-MarketProfit"
    OTHER = "SOW-IND-Other"
    PENSION = "SOW-IND-Pension"
    PROPERTY = "SOW-IND-Property"


class ProofOfAddressTypeEnum(ExtendedEnum):
    BANK_STATEMENT = "Bank Statement"
    BROKERAGE_STATEMENT = "Brokerage Statement"
    HOMEOWNER_INSURANCE_POLICY_BILL = "Homeowner Insurance Policy Bill"
    HOMEOWNER_INSURANCE_POLICY_DOCUMENT = "Homeowner Insurance Policy Document"
    RENTER_INSURANCE_POLICY_BILL = "Renter Insurance Policy bill"
    RENTER_INSURANCE_POLICY_DOCUMENT = "Renter Insurance Policy Document"
    SECURITY_SYSTEM_BILL = "Security System Bill"
    GOVERNMENT_ISSUED_LETTERS = "Government Issued Letters"
    UTILITY_BILL = "Utility Bill"
    CURRENT_LEASE = "Current Lease"
    EVIDENCE_OF_OWNERSHIP_OF_PROPERTY = "Evidence of Ownership of Property"
    DRIVER_LICENSE = "Driver License"
    OTHER_DOCUMENT = "Other Document"
