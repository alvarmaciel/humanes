from dataclasses import dataclass, field
from datetime import date
from enum import Enum


class AccountType(Enum):
    ADHERENTE = "adherente"
    HUMANE = "humane"


@dataclass
class AccountData:
    name: str
    last_name: str
    venture: str
    dni: str
    zip_code: str
    address: str
    phone: str
    email: str

@dataclass
class Account:
    account_data: AccountData
    socie_type: AccountType = field(default=None)
    fees: list[dict] = field(default_factory=list)
    invoices: list[dict] = field(default_factory=list)
    activated: bool = field(default=True)
    socie: bool = field(default=True)
    provider: bool = field(default=False)

    @property
    def is_provider(self):
        return self.provider
    @property
    def is_socie(self):
        return self.socie

    def get_status(self, today: date) -> bool:
        if not self.is_socie:
            return
        if self._check_and_update_status(today):
            self.activated = True
        else:
            self.activated = False
        return self.activated

    def _check_and_update_status(self, today: date) -> bool:
        last_cuota = self.fees[-1]
        last_cuota_date = last_cuota["date"]
        difference = today - last_cuota_date
        if difference.days >= 90:
            return False
        else:
            return True
