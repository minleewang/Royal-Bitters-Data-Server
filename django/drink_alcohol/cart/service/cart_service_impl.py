from django.db.models import OuterRef, Subquery, Value
from django.db.models.functions import Coalesce
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from account.repository.account_repository_impl import AccountRepositoryImpl
from alcohol.repository.alcohol_repository_impl import AlcoholRepositoryImpl
from cart.entity.cart import Cart
from cart.repository.cart_repository_impl import CartRepositoryImpl
from cart.service.cart_service import CartService


class CartServiceImpl(CartService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__cartRepository = CartRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
            cls.__instance.__alcoholRepository = AlcoholRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createCart(self, accountId, cart):
        foundAccount = self.__accountRepository.findById(accountId)
        # id = accountId
        # id(번호)로 매칭되는 소비자(계정) 검색해서 foundAccount에 저장

        if not foundAccount:
            raise Exception("해당 accountId에 해당하는 account를 찾을 수 없습니다.")

        foundAlcohol = self.__alcoholRepository.findById(cart["id"])
        # findById는 Alcohol 테이블에서 ID가 cart["id"]인 데이터를 조회합니다.
        # cart["id"]: 이 값은 장바구니(cart) 데이터에서 전달된 id로,
        # 장바구니에 담긴 특정 Alcohol 항목의 ID를 나타냅니다.


        if not foundAlcohol:
            raise Exception("해당 AlcoholId에 해당하는 주류를 찾을 수 없습니다.")


        # 장바구니(Cart)에 항목을 추가하거나 업데이트
        # 사용자의 장바구니에 동일한 상품(Alcohol)이 이미 존재하는지 확인하고, 존재하면 수량을 업데이트하는 것
        foundCart = self.__cartRepository.findCartByAccountAndAlcohol(foundAccount, foundAlcohol)
        # 특정 사용자(foundAccount)의 장바구니에서 특정 술(foundAlcohol) 항목을 조회

        if foundCart:  # 조회된 장바구니 항목(foundCart)이 존재하는지 확인
            foundCart.quantity += cart["quantity"]
            # 존재하는 경우: 기존 항목의 수량(quantity)을 업데이트
            updatedCart = self.__cartRepository.save(foundCart)
            # 업데이트된 장바구니 항목을 데이터베이스에 저장
            return updatedCart

        newCart = Cart(
            account=foundAccount,
            alcohol=foundAlcohol,
            quantity=cart["quantity"]
        )
        savedCart = self.__cartRepository.save(newCart)
        return savedCart

    def listCart(self, accountId, page, pageSize):
        try:
            print(f"listCart() pageSize: {pageSize}")

            # Account 확인
            account = self.__accountRepository.findById(accountId)
            if not account:
                raise ValueError(f"Account with ID {accountId} not found.")
            print(f"Account found: {account}")

            # Cart 목록 가져오기 (페이지네이션 적용된 결과)
            paginatedCartList = self.__cartRepository.findCartByAccount(account, page, pageSize)
            print(f"Paginated cart list query: {paginatedCartList}")

            # 전체 아이템 수 계산
            total_items = paginatedCartList.paginator.count  # Paginator에서 count 값을 사용

            # 필요한 데이터만 추출
            cartDataList = [
                {
                    "id": cart.id,
                    "title": cart.alcohol.title,
                    "price": cart.alcohol.price,
                    #"image": cart.image,
                    "quantity": cart.quantity,
                }
                for cart in paginatedCartList
            ]

            print(f"Total items: {total_items}")
            print(f"Page items: {len(cartDataList)}")

            return cartDataList, total_items  # total_items를 반환

        except Exception as e:
            print(f"Unexpected error in listCart: {e}")
            raise

    def removeCart(self, accountId, cartId):
        try:
            cart = self.__cartRepository.findById(cartId)
            print(f"cart: {cart}")
            if cart is None or str(cart.account.id) != str(accountId):
                return {
                    "error": "해당 카트를 찾을 수 없거나 소유자가 일치하지 않습니다.",
                    "success": False
                }

            result = self.__cartRepository.deleteById(cartId)
            if result:
                return {
                    "success": True,
                    "message": "카트 항목이 삭제되었습니다."
                }

        except Exception as e:
            print(f"Error in CartService.removeCart: {e}")
            return {
                "error": "서버 내부 오류",
                "success": False
            }
