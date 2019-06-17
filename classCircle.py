import turtle as tt
import random as rd
from math import pi

class Circle(object):
	"""docstring for Circle"""
	def __init__(self, radius,maxX,maxY,minX,minY):
		self.radius = radius
		self.centerX = rd.randint(minX,maxX) # random coordinate on x from minX<=randomX<=maxX
		self.centerY = rd.randint(minY,maxY) # random coordinate on y from minY<=randomY<=maxY
		self.area = (pi)*(radius**2)
		

	def draw(self):
		tt.penup() #pen is up
		tt.pencolor('black') #color of drawing
		tt.pensize(3)#width of the pen
		tt.fillcolor('blue')#color of all circle's area
		tt.goto(self.centerX,self.centerY-self.radius)#moves to point (centerX,centerY-radius)
		tt.pendown()#pen is ready for draw
		tt.begin_fill()
		tt.circle(self.radius) #it multiplies because it doesn't start to draw in the origin
		tt.end_fill()
		tt.pencolor('red') #color of drawing
		tt.penup() #pen is up
		tt.goto(self.centerX,self.centerY)
		tt.pendown()#pen is ready for draw
		tt.dot()



	def generaAspersores(numAspersores,radio,maxX,maxY,minX,minY):
		"""
		input args
		radio = radius of the circles to be drawn
		limx = maximum limit of the values on x for the origin of the circle
		limy = maximum limit of the values on y for the origin of the circle
		"""
		aspersores = []
		for i in range(numAspersores):
			randomX = rd.randint(minX,maxX) # random coordinate on x from minX<=randomX<=maxX
			randomY = rd.randint(minY,maxY) # random coordinate on y from minY<=randomY<=maxY
			#aspersor = Circle(radio,randomX,randomY)
			#aspersores.append(aspersor)
			#aspersor.draw()

		return aspersores

	def drawAxis_aspersores(self,axes,numAxis):
		ejes = axes[numAxis]
		tt.penup() #pen is up
		tt.pencolor('black') #color of drawing
		tt.pensize(3)#width of the pen
		tt.fillcolor('blue')#color of all circle's area
		tt.goto(ejes[0],ejes[1]-self.radius)#moves to point (centerX,centerY-radius)
		tt.pendown()#pen is ready for draw
		tt.begin_fill()
		tt.circle(self.radius) #it multiplies because it doesn't start to draw in the origin
		tt.end_fill()
		tt.pencolor('red') #color of drawing
		tt.penup() #pen is up
		tt.goto(ejes[0],ejes[1])
		tt.pendown()#pen is ready for draw
		tt.dot()

		
			

	def euclideanDistance(self):
		pass