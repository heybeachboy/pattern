"""
test interface for python
"""
from abc import ABCMeta,abstractmethod

class Trade(metaclass=ABCMeta):
	@abstractmethod
	def pay(self, num):
		pass

class WeiXinPay(Trade):
	def pay(self, num):
		print("WeiXin Pay %d $"%num)

class AliPay(Trade):
	def pay(self, num):
		print("Ali Pay %d $"%num)

obj = WeiXinPay()
obj.pay(23)
obj = AliPay()
obj.pay(56)
