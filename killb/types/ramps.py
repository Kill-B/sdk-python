from typing import TypedDict, Optional, Any, Union
from enum import Enum
from killb.types.quotations import FromCurrency, ToCurrency, CashInMethod, CashOutMethod


class RefundInstructions(TypedDict, total=False):
    network: Optional[str]
    address: Optional[str]
    asset: Optional[str]
    clabe: Optional[str]
    beneficiary: Optional[str]


class CreateRampData(TypedDict, total=False):
    quotationId: str
    userId: str
    accountId: str
    refundInstructions: Optional[RefundInstructions]


class GetRampQuery(TypedDict, total=False):
    limit: Optional[int]
    page: Optional[int]
    id: Optional[str]
    externalId: Optional[str]
    status: Optional[str]


class CreateRampResponse(TypedDict, total=False):
    id: str
    active: bool
    fromCurrency: FromCurrency
    toCurrency: ToCurrency
    fromAmount: Union[int, float]
    toAmount: Union[int, float]
    quotationId: str
    userId: str
    cashInMethod: CashInMethod
    cashOutMethod: CashOutMethod
    accountId: str
    isPrefunded: Optional[bool]
    paymentInfo: Any
    details: str
    transferProof: str
    type: str
    createdAt: str
    updatedAt: str


class GetRampQueryResponse(TypedDict, total=False):
    totalPage: int
    ramps: list[CreateRampResponse]
