from typing import TypedDict, Optional, List, Union
from enum import Enum


class PSEAccountType(Enum):
    SAVINGS = "savings"
    CHECKING = "checking"


class DocumentType(Enum):
    PASSPORT = "PASSPORT"
    DRIVER_LICENSE = "DRIVER_LICENSE"
    NUIP = "NUIP"
    RFC = "RFC"
    SSN = "SSN"
    CURP = "CURP"
    CPF = "CPF"
    INE = "INE"
    IFE = "IFE"


class WalletCurrency(Enum):
    USDC = "USDC"
    USDT = "USDT"


class WalletNetwork(Enum):
    POLYGON = "POLYGON"


class PSEDocumentType(TypedDict, total=False):
    type: DocumentType
    number: str
    issuedCountryCode: str
    expeditionDate: str
    cic: Optional[str]
    identificadorCiudadano: Optional[str]
    ocr: Optional[str]
    numeroEmision: Optional[str]


class PSEAccount(TypedDict, total=False):
    firstName: str
    middleName: Optional[str]
    lastName: str
    companyName: Optional[str]
    email: str
    phone: str
    accountNumber: str
    bankCode: str
    type: PSEAccountType
    countryCode: str
    document: PSEDocumentType


class PSEAccountUpdate(TypedDict, total=False):
    accountNumber: str
    bankCode: str
    type: PSEAccountType
    document: PSEDocumentType


class WalletAccount(TypedDict, total=False):
    firstName: str
    middleName: Optional[str]
    lastName: str
    companyName: Optional[str]
    email: str
    phone: str
    document: PSEDocumentType
    currency: WalletCurrency
    network: WalletNetwork
    address: str


class WalletAccountUpdate(TypedDict, total=False):
    document: PSEDocumentType
    currency: WalletCurrency
    network: WalletNetwork
    address: str

    
class SPEIAccount(TypedDict, total=False):
    firstName: str
    middleName: Optional[str]
    lastName: str
    companyName: Optional[str]
    email: str
    phone: str
    document: PSEDocumentType
    clabe: str
    clabeType: Optional[str]
    bankCode: Optional[str]
    countryCode: str


class SPEIAccountUpdate(TypedDict, total=False):
    document: PSEDocumentType
    clabe: Optional[str]
    clabeType: Optional[str]


class AccountData(TypedDict, total=False):
    type: str
    userId: str
    data: Union[WalletAccount, PSEAccount, SPEIAccount]
    externalId: Optional[str]


class AccountUpdateData(TypedDict, total=False):
    type: str
    data: Union[SPEIAccountUpdate, WalletAccountUpdate, PSEAccountUpdate]


class AccountGetByQuery(TypedDict, total=False):
    userId: Optional[str]
    type: Optional[str]
    accountNumber: Optional[str]
    routingNumber: Optional[str]
    address: Optional[str]
    clabe: Optional[str]
    cvu: Optional[str]
    limit: Optional[int]
    page: Optional[int]


class AccountByQueryResponse(TypedDict, total=False):
    id: str
    userId: str
    type: str
    data: Union[PSEAccount, WalletAccount, SPEIAccount]
    createdAt: str
    updatedAt: str


class AccountGetByQueryResponse(TypedDict, total=False):
    totalPage: int
    accounts: List[AccountByQueryResponse]


class AccountCreateResponse(TypedDict, total=False):
    id: str
    userId: str
    type: str
    status: str
    data: Union[WalletAccount, PSEAccount, SPEIAccount]
    externalId: Optional[str]
    createdAt: str
    updatedAt: str