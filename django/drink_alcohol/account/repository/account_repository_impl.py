from django.core.exceptions import ObjectDoesNotExist

from account.entity.account import Account
from account.repository.account_repository import AccountRepository


class AccountRepositoryImpl(AccountRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def save(self, email):
        account = Account(email=email)
        account.save()
        return account
    # email만으로 Customer (소비자) 식별


    def findById(self, accountId):
        try:
            return Account.objects.get(id=accountId)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist(f"Account ID {accountId} 존재하지 않음.")

    def findByEmail(self, email):
        try:
            return Account.objects.get(email=email)
        except ObjectDoesNotExist:
            raise ObjectDoesNotExist(f"Account {email} 존재하지 않음.")

