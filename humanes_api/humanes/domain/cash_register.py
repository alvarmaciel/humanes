from dataclasses import dataclass, field
from decimal import Decimal
from humanes.domain.socies import Account
@dataclass
class CashRegister:
    total: Decimal = 0
    invoices : list[dict] = field(default_factory=list)


class Cashier:
    def __init__(self, cashier: Account, caja: CashRegister=None):
        self.cashier = cashier
        self.caja = caja

    def checkout(self, socie, today, cuota, caja):
        caja.total += cuota["amount"]
        caja.invoices.append({"socie": socie, "date": today, "amount": cuota["amount"]})
        socie.fees.append(cuota)
        socie.invoices.append({"socie": socie, "date": today, "amount": cuota["amount"]})
    def get_all_invoices_by_socie(self, socie:Account)->list:
        result = []
        for invoice in self.caja.invoices:
            if invoice["socie"] == socie:
                result.append(invoice)
        return result
