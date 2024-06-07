from typing import TypedDict, Optional, List, Union
from enum import Enum


class FromCurrency(Enum):
    MXN = "MXN"
    COP = "COP"
    USDC = "USDC"
    USDT = "USDT"


class ToCurrency(Enum):
    MXN = "MXN"
    COP = "COP"
    USDC = "USDC"
    USDT = "USDT"


class CashInMethod(Enum):
    SPEI = 'SPEI'
    POLYGON = 'POLYGON'
    ERC20 = 'ERC20'
    PSE = 'PSE'
    PRE_FUND = 'PRE_FUND'


class CashOutMethod(Enum):
    SPEI = 'SPEI'
    POLYGON = 'POLYGON'
    ERC20 = 'ERC20'
    PSE = 'PSE'


class CreateQuotation(TypedDict, total=False):
    fromCurrency: FromCurrency
    toCurrency: ToCurrency
    amount: int
    amountIsToCurrency: bool
    cashInMethod: CashInMethod
    cashOutMethod: CashOutMethod
    skipOrder: Optional[int]


class CreateQuotationResponse(TypedDict, total=False):
    id: str
    fromCurrency: FromCurrency
    toCurrency: ToCurrency
    fromAmount: int
    toAmount: int
    rate: int
    expiresAt: int
    cashInMethod: CashInMethod
    cashOutMethod: CashOutMethod


class SimulateQuotationResponse(TypedDict, total=False):
    fromCurrency: FromCurrency
    toCurrency: ToCurrency
    fromAmount: int
    toAmount: int
    rate: int
    cashInMethod: CashInMethod
    cashOutMethod: CashOutMethod
