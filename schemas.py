from datetime import datetime
from pydantic import BaseModel


class AccountCreate(BaseModel):
    name: str
    balance: int = 0


class TransactionCreate(BaseModel):
    account_id: int
    category_id: int | None = None
    amount: int
    memo: str | None = None


class TransactionRead(BaseModel):
    id: int
    account_id: int
    category_id: int | None
    amount: int
    memo: str | None
    occurred_at: datetime

    model_config = {"from_attributes": True}


class AccountRead(BaseModel):
    id: int
    name: str
    balance: int

    model_config = {"from_attributes": True}


class AccountReadWithTx(AccountRead):
    transactions: list[TransactionRead] = []