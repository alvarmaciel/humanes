from typing import List, Optional

from pydantic import BaseModel, Field


class AccountDataModel(BaseModel):
    id: int
    name: str
    last_name: str
    venture: Optional[str] = ""
    dni: str
    zip_code: str
    address: str
    phone: str
    email: str


class AccountModel(BaseModel):
    id: int
    account_data_id: int
    socie_type: str
    fees: Optional[List[dict]] = Field(default_factory=list)
    invoices: Optional[List[dict]] = Field(default_factory=list)
    activated: bool = True
    socie: bool = True
    provider: bool = False
