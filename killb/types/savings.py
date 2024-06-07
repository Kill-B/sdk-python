from typing import TypedDict, Optional, Any, Union
from enum import Enum


class SavingsStatus(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class SavingsDepositInstructionsType(Enum):
    ACH = "ACH"
    WIRE = "WIRE"


class SavingsWithdrawalStatus(Enum):
    CREATED = 'CREATED'
    PENDING = 'PENDING'
    PROCESSING = 'PROCESSING'
    CONFIRMED = 'CONFIRMED'
    REFUNDED = 'REFUNDED'
    COMPLETED = 'COMPLETED'
    CANCELED = 'CANCELED'
    EXPIRED = 'EXPIRED'
    FAILED = 'FAILED'
    ERROR = 'ERROR'
    REJECTED = 'REJECTED'


class SavingsCreateResponse(TypedDict, total=False):
    id: str
    userId: str
    status: SavingsStatus
    createdAt: str
    updatedAt: str


class SavingsWithdrawalSourceData(TypedDict, total=False):
    savingsAccountId: str


class SavingsWithdrawalDestinationData(TypedDict, total=False):
    savingsAccountId: Optional[str]
    externalAccountId: Optional[str]


class SavingsWithdrawalData(TypedDict, total=False):
    source: SavingsWithdrawalSourceData
    destination: SavingsWithdrawalDestinationData
    amount: int
    comment: Optional[str]


class SourceReturn(TypedDict, total=False):
    currency: str
    custodialAccountId: str


class DestinationReturn(TypedDict, total=False):
    currency: str
    externalAccountId: str


class SavingsGetTransactions(TypedDict, total=False):
    limit: Optional[int]
    page: Optional[int]
    id: Optional[str]
    destinationAccountId: Optional[str]
    originAccountId: Optional[str]
    userId: Optional[str]
    type: Optional[str]


class SavingsGetTransactionReturn(TypedDict, total=False):
    id: str
    customerId: str
    userId: str
    originAccountId: str
    destinationAccountId: str
    amount: str
    type: str
    currency: str
    createdAt: str
    updatedAt: str


class SavingsWithdrawalReturn(TypedDict, total=False):
    id: str
    status: SavingsWithdrawalStatus
    amount: Union[int, float]
    userId: str
    type: str
    source: SourceReturn
    destination: DestinationReturn
    createdAt: str
    updatedAt: str


class SavingsGetBalanceReturn(TypedDict, total=False):
    currency: str
    amount: int


class SavingsGetDepositInstructions(TypedDict, total=False):
    savings_account_id: str
    type: SavingsDepositInstructionsType


class SavingsGetDepositInstructionsReturn(TypedDict, total=False):
    type: SavingsDepositInstructionsType
    currency: str
    bankName: str
    bankAddress: Any
    routingNumber: str
    accountNumber: str
    depositMessage: Optional[str]
    bankBeneficiaryName: Optional[str]
