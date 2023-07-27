from typing import Protocol, TypeVar, Union, runtime_checkable

from humanes_api.humanes.domain.socies import AccountData, Account

T = TypeVar('T', bound=Union[AccountData, Account])
@runtime_checkable
class Repository(Protocol[T]):
    def add(self, *args, **kwargs) -> None:
        ...
    def get(self, *args, **kwargs) -> T | None:
        ...


class AccountDataRepository:
    def __init__(self, session):
        self.session = session

    def add(self, account_data):
        self.session.add(account_data)

    def get(self, reference):
        return self.session.query(AccountData).filter_by(dni=reference).one()

    def list(self):
        return self.session.query(AccountData).all()