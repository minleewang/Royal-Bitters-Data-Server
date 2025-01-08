from abc import ABC, abstractmethod


class CartRepository(ABC):

    @abstractmethod
    def save(self, cart):
        pass

    @abstractmethod
    def findCartByAccountAndAlcohol(self, account, alcohol):
        pass

    @abstractmethod
    def findCartByAccount(self, account, page, limit):
        pass

    @abstractmethod
    def findById(self, cartId):
        pass

    @abstractmethod
    def deleteById(self, cartId):
        pass