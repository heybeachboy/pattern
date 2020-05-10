"""
Factory Pattern
"""
from abc import ABCMeta,abstractmethod

class Shape(metaclass = ABCMeta):
	@abstractmethod
	def draw():
		pass

class Rectangle(Shape):
	def draw(self):
		print("make a rectanle object")

class Square(Shape):
	def draw(self):
		print("make a square object")

class Circle(Shape):
	def draw(self):
		print("make a circle object")

class ShapeFactory():
      def __init__(self, name):
	      self.name = name

      def GetObject(self):
	      return self.__makeShapeObj()
	      
      def __makeShapeObj(self):
	      if self.name == "rectangle":
		      return Rectangle()
	      if self.name == "square":
		      return Square()
	      if self.name == "circle":
		      return Circle()
	      print("unknow object:%s"%(self.name))
	      return None
if __name__ == "__main__":
	obj1 = ShapeFactory("rectangle")
	obj1.GetObject().draw()

	obj2 = ShapeFactory("square")
	obj2.GetObject().draw()

	obj3 = ShapeFactory("circle")
	obj3.GetObject().draw()
