from typing import TypedDict, Optional, List, Union
from enum import Enum
from killb.types.account import DocumentType


class UserType(Enum):
    PERSON = "PERSON"
    COMPANY = "COMPANY"


class AddressData(TypedDict, total=False):
    street1: str
    street2: Optional[str]
    city: str
    state: str
    zipCode: str
    countryCode: str


class PersonDocumentData(TypedDict, total=False):
    type: DocumentType
    number: str
    issuedCountryCode: str


class PersonData(TypedDict, total=False):
    firstName: str
    middleName: Optional[str]
    lastName: str
    dateOfBirth: str
    email: str
    phone: str
    address: AddressData
    document: PersonDocumentData


class CompanyData(TypedDict, total=False):
    companyName: str
    tradeName: Optional[str]
    legalStructure: Optional[str]
    description: Optional[str]
    establishedOn: Optional[str]
    phone: Optional[str]
    address: AddressData
    mainOwnerUser: str
    ownerUsers: Optional[List[str]]
    naics: Optional[str]
    naicsDescription: Optional[str]
    document: PersonDocumentData


class GetUserByQuery(TypedDict, total=False):
    limit: Optional[int]
    page: Optional[int]
    id: Optional[str]
    firstName: Optional[str]
    middleName: Optional[str]
    lastName: Optional[str]
    dateOfBirth: Optional[str]
    externalId: Optional[str]
    companyName: Optional[str]
    tradeName: Optional[str]
    legalStructure: Optional[str]
    description: Optional[str]
    establishedOn: Optional[str]
    email: Optional[str]
    mainOwnerUser: Optional[str]
    ownerUsers: Optional[List[str]]
    naics: Optional[str]
    naicsDescription: Optional[str]


class UserCreateData(TypedDict, total=False):
    type: UserType
    data: Union[PersonData, CompanyData]
    externalId: Optional[str]


class UserUpdateData(TypedDict, total=False):
    data: Union[PersonData, CompanyData]


class UserCreateResponse(TypedDict, total=False):
    id: str
    customerId: str
    type: UserType
    data: Union[PersonData, CompanyData]
    externalId: Optional[str]
    accessLevel: str
    active: bool
    createdAt: str
    updatedAt: str
