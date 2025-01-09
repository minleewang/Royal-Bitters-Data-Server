from django.db import transaction

from account.repository.account_repository_impl import AccountRepositoryImpl
from alcohol.repository.alcohol_repository_impl import AlcoholRepositoryImpl
from cart.repository.cart_repository_impl import CartRepositoryImpl

from orders.entity.orders import Orders
from orders.entity.orders_items import OrdersItems
from orders.entity.orders_status import OrdersStatus
from orders.repository.order_item_repository_impl import OrderItemRepositoryImpl
from orders.repository.order_repository_impl import OrderRepositoryImpl
from orders.service.order_service import OrderService


class OrderServiceImpl(OrderService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__cartRepository = CartRepositoryImpl.getInstance()
            cls.__instance.__orderRepository = OrderRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
            cls.__instance.__orderItemRepository = OrderItemRepositoryImpl.getInstance()
            cls.__instance.__alcoholRepository = AlcoholRepositoryImpl.getInstance()


        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    @transaction.atomic # Django의 트랜잭션 관리 기능/ 효과: 작업 중 하나라도 실패하면 전체 작업이 롤백
    def createOrder(self, accountId, items, total):
        # accountId= id
        # items: Order에 포함된 항목 리스트. 각 항목은 딕셔너리 형태로 전달
        # total: 주문 총 금액

        # 계정 조회 및 검증
        account = self.__accountRepository.findById(accountId)
        # accountId를 기반으로 사용자 계정을 조회
        if not account:
            raise Exception(f"Account id {accountId} 존재하지 않음.")

        # 2. 총 금액 검증
        if not isinstance(total, (int, float)) or total <= 0:
            raise Exception("유효하지 않은 총 금액입니다.")

        # 3. 주문 항목 검증
        if not items or not isinstance(items, list): # items가 리스트인지 확인
            raise Exception("유효하지 않은 주문 항목입니다.")
            # 리스트가 비어 있거나 올바르지 않으면 예외를 발생시킴

        # 주문 생성
        orders = Orders(
            account=account,
            total_amount=total,
            status=OrdersStatus.PENDING,
        )
        orders = self.__orderRepository.save(orders)
        # self.__orderRepository.save(orders)를 통해 데이터베이스에 저장하고,
        print(f"order 생성: {orders}") # 저장된 객체를 반환받음

        orderItemList = []

        # 주문 항목 생성 : 주문 항목 데이터를 순회하며 처리
        for item in items:
            cartItem = self.__cartRepository.findById(item["id"])
            # item["id"]로 장바구니 항목을 조회
            if not cartItem: # 존재하지 않으면 예외 발생.
                raise Exception(f"Cart item ID {item['id']} 존재하지 않음.")

            '''''
            gameSoftware = cartItem.getGameSoftware()
            # 장바구니 항목에서 게임 소프트웨어를 가져옴
             if not gameSoftware: # 없으면 존재하지 않는다고 반환
                raise Exception(f"Game software with ID {gameSoftware.getId()} 존재하지 않음.")
            '''
            alcohol = cartItem.getAlcohol()
            # 장바구니 항목에서 게임 구매할 술을 가져옴
            if not alcohol:
                raise Exception(f"Alcohol with ID {alcohol.getId()} 존재하지 않음.")

            # #게임 소프트웨어 가격 조회
            #gameSoftwarePrice = self.__gameSoftwarePriceRepository.findByGameSoftware(gameSoftware)
            # 이 코드는 __gameSoftwarePriceRepository 객체의 findByGameSoftware 메서드를 호출하여,
            # 특정 gameSoftware와 관련된 가격 데이터를 조회하고,
            # 결과를 gameSoftwarePrice 변수에 저장하는 역할을 합니다.

            # alcohol 가격 조회
            alcoholPrice = self.__alcoholRepository.findPriceById(accountId)


            # 주문 항목 생성
            orderItem = OrdersItems(
                orders=orders,  # orders가 올바르게 연결되었는지 확인
                alcoholTitle= alcohol, # alcohol = cartItem.getAlcohol()
                quantity=item["quantity"],
                price=alcoholPrice * item["quantity"],
            )
            orderItemList.append(orderItem)

        print(f"orderItemList: {orderItemList}")

        # 주문 항목 저장
        if orderItemList:
            self.__orderItemRepository.bulkCreate(orderItemList)

        return orders.getId()