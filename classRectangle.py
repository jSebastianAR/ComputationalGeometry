import turtle as tt
import time as tm
#This class represents all the irrigation field

class Rectangle():
	"""docstring for rectangle"""
	def __init__(self, x,y):
		#super(rectangle, self).__init__()
		#Axis located on the origin of the plane i.e (0,0)
		self.ejex1 = -(x/2) #both values contains the minimum values for x and y, are the negative bound
		self.ejey1 = -(y/2)
		self.minX = self.ejex1
		self.minY = self.ejey1
		#Axis located on top of the ejex1 and ejey1 i.e (0,y)
		self.ejex2 = -(x/2)
		self.ejey2 = (y/2)
		#Axis located on coordinate (x,y)
		self.ejex3 = (x/2) #both values contains the maximum values for x and y, are the positive bound
		self.ejey3 = (y/2)
		self.maxX = self.ejex3
		self.maxY = self.ejey3
		#Axis located on coordinate (x,0)
		self.ejex4 = (x/2)
		self.ejey4 = -(y/2)
		self.base = x
		self.altura = y
		self.area = x*y
		
	def draw(self):
		tt.hideturtle()
		tt.penup() #pen is up 
		tt.pensize(5)
		tt.fillcolor('green')
		tt.goto(self.ejex1,self.ejey1) # goes to origin
		tt.pendown() #pen is ready for draw
		tt.begin_fill()
		tt.goto(self.ejex2,self.ejey2)
		tm.sleep(.5)
		tt.goto(self.ejex3,self.ejey3)
		tm.sleep(.5)
		tt.goto(self.ejex4,self.ejey4)
		tm.sleep(.5)
		tt.goto(self.ejex1,self.ejey1) # returns to origin
		tt.end_fill()


	def getx1(self,eje):
			self.ejex1 = eje 


		
		

