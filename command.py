""""
Command Pattern with Python Code
"""
from abc import abstractmethod,ABCMeta

class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

class Stock():
    _name = "ABC"
    _quantity = 20
    
    def buy(self):
        print("Stock [Name :{0}, Quantity: {1}] bought.".format(self._name, self._quantity))

    def sell(self):
        print("Stock [Name :{0}, Quantity: {1}] sold.".format(self._name, self._quantity))

class BuyStock(Order):
    _abcStock = None
    def __init__(self, inStock):
        self._abcStock = inStock

    def execute(self):
        self._abcStock.buy()
class SellStock(Order):
    _abcStock = None

    def __init__(self, inStock):
        self._abcStock = inStock

    def execute(self):
        self._abcStock.sell()

class Broker():
     _orderList = []
     
     def takeOrder(self, inOrder):
         self._orderList.append(inOrder)
     
     def placeOrder(self):
         for order in self._orderList:
             order.execute()
         self._orderList.clear()

if __name__ == "__main__":
    stock = Stock()
    buyAction = BuyStock(stock)
    sellAction = SellStock(stock)

    broker = Broker()
    broker.takeOrder(buyAction)
    broker.takeOrder(sellAction)
    broker.placeOrder()
