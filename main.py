from classRectangle import *
#from classCircle import *
from classCircle import *
import turtle as tt
from math import pi

def updateCenterInBase(i,axes,firstCircleInEdge,radioC,currentCenterX):
	currentCenterY = axes[i][1]
	if(firstCircleInEdge==1):
		#initialize both values for the centre in te above edge, goes from left to the right
		currentCenterX = axes[i][0]+(2*radioC) 
		firstCircleInEdge=firstCircleInEdge+1 #adds
	else:
		currentCenterX = currentCenterX+(2*radioC) 

	return currentCenterX,currentCenterY

def updateCenterInHeight(i,axes,firstCircleInEdge,radioC,currentCenterY):
	currentCenterX = axes[i][0] 
	if(firstCircleInEdge==1):
		#initialize both values for the centre in te above edge, goes from left to the right
		currentCenterY = axes[i][1]-(2*radioC)
		firstCircleInEdge=firstCircleInEdge+1 #adds
	else:
		currentCenterY = currentCenterY-(2*radioC)

	return currentCenterX,currentCenterY

def moveCircle(aspersor,i,axes,firstCircleInEdge,radioC,currentCenterX,chosedEdge):
	currentCenterX,aspersor.centerY = updateCenterInBase(i,axes,firstCircleInEdge,radioC,currentCenterX)
	aspersor.centerX = currentCenterX
	aspersor.draw()
	if firstCircleInEdge==aspersoresBase:
		chosedEdge = chosedEdge+1 #pass to base bottom edge	
		firstCircleInEdge = 1
	else:
		firstCircleInEdge = firstCircleInEdge+1	

	return firstCircleInEdge



def updateAllNewVariables(radioC,axes,n,x,y):
	espacioBase = x-(2*n*radioC) #gets the remaining space in base after add the circles on each axis over the base
	espacioAltura = y-(2*n*radioC) #gets the remaining space in base after add the circles on each axis over the height
	aspersoresBase = round(espacioBase/(2*radioC))
	aspersoresAltura = round(espacioAltura/(2*radioC))
	if aspersoresBase < 1: #if the round is less than 1
		aspersoresBase = 1
	if aspersoresAltura < 1:
		aspersoresAltura = 1
	#print("base: %f altura %f"%(aspersoresBase,aspersoresAltura))
	print("base: %d altura %d iteracion %d"%(aspersoresBase,aspersoresAltura,n))
	axes[0][0] = axes[0][0]+radioC
	axes[0][1] = axes[0][1]+radioC
	axes[1][0] = axes[1][0]+radioC
	axes[1][1] = axes[1][1]-radioC
	axes[2][0] = axes[2][0]-radioC
	axes[2][1] = axes[2][1]-radioC
	axes[3][0] = axes[3][0]-radioC
	axes[3][1] = axes[3][1]+radioC
	return aspersoresBase,aspersoresAltura,axes

def lastCircles(axes,aspersor,numRectangulos):
	centerX = axes[0][0]
	centerY = axes[0][1]
	for i in range(numRectangulos):
		aspersor.centerX = centerX
		aspersor.centerY = centerY
		centerX = centerX+(2*aspersor.radius)
		aspersor.draw()



opcion=1
while (opcion!=0):
	x = int(input('Ingresa el largo del campo '))
	y = int(input('Ingresa el ancho del campo '))


	campo = Rectangle(x,y)

	print("Ejes 1: (%d,%d)"%(campo.ejex1,campo.ejey1))
	print("Ejes 2: (%d,%d)"%(campo.ejex2,campo.ejey2))
	print("Ejes 3: (%d,%d)"%(campo.ejex3,campo.ejey3))
	print("Ejes 4: (%d,%d)"%(campo.ejex4,campo.ejey4))
	axes = [[campo.ejex1,campo.ejey1],[campo.ejex2,campo.ejey2],[campo.ejex3,campo.ejey3],[campo.ejex4,campo.ejey4]]	
	print(axes[0][0])
	tt.screensize(500,500)
	campo.draw()
	print("Campo de %d*%d con area = %d"%(campo.base,campo.altura,campo.area))

	aspersores = []
	radioC = int(input('Ingresa el radio de los aspersores: '))
	aspersores_area = (pi)*(radioC**2)
	numAspersores = (campo.area/aspersores_area)-4
	#print('El número aproximado de aspersores para este campo es = %d'%(numAspersores))
	#input('')

	#FOR DRAW IN EDGES
	espacioBase = x-(2*radioC) #gets the remaining space in base after add the circles on each axis over the base
	espacioAltura = y-(2*radioC) #gets the remaining space in base after add the circles on each axis over the height
	aspersoresBase = round(espacioBase/(2*radioC))
	aspersoresAltura = round(espacioAltura/(2*radioC))
	

	#print("base: %f altura %f"%(aspersoresBase,aspersoresAltura))
	#print("base: %d altura %d"%(aspersoresBase,aspersoresAltura))
	drawIn_Edges = False
	chosedEdge = 1
	firstCircleInEdge = 1
	currentCenterX = 0
	currentCenterY = 0
	#FOR DRAW IN EDGES	
	numberIterations = 1;
	indexAxis = 0;
	update = False
	r = espacioAltura = y-(4*radioC);
	numRectangulos = round(r/(2*radioC))+3
	#for i in range(int(numRectangulos)):
	AspersoresDibujados = 0
	DrawedRectangles = 0	
	isOne = False
	flag = False
	while DrawedRectangles<numRectangulos :
		aspersor = Circle(radioC,campo.maxX,campo.maxY,campo.minX,campo.minY)
		#print("i = %d"%(i))
		if(drawIn_Edges==False and update==False): #draw in axes
			#input('')
			if(indexAxis==4):
				drawIn_Edges = True
			else:	
				aspersor.centerX = axes[indexAxis][0]
				aspersor.centerY = axes[indexAxis][1]
				aspersor.draw()	
				indexAxis = indexAxis+1

		elif drawIn_Edges==True and update==False: #Ready for draw in edges
			#input('')
			if(chosedEdge==1):
				currentCenterX,aspersor.centerY = updateCenterInBase(0,axes,firstCircleInEdge,radioC,currentCenterX)
				aspersor.centerX = currentCenterX
				aspersor.draw()
				if firstCircleInEdge==aspersoresBase:
					chosedEdge = 2 #pass to base bottom edge	
					firstCircleInEdge = 1
				else:
					firstCircleInEdge = firstCircleInEdge+1

			elif(chosedEdge==2):
				currentCenterX,aspersor.centerY = updateCenterInBase(1,axes,firstCircleInEdge,radioC,currentCenterX)
				aspersor.centerX = currentCenterX
				aspersor.draw()
				if firstCircleInEdge==aspersoresBase:
					chosedEdge = 3 #pass to base bottom edge
					firstCircleInEdge = 1
				else:
					firstCircleInEdge = firstCircleInEdge+1
			elif(chosedEdge==3):
				aspersor.centerX,currentCenterY = updateCenterInHeight(1,axes,firstCircleInEdge,radioC,currentCenterY)
				aspersor.centerY = currentCenterY
				aspersor.draw()
				if firstCircleInEdge==aspersoresAltura:
					chosedEdge = 4 #pass to base bottom edge
					firstCircleInEdge = 1
				else:
					firstCircleInEdge = firstCircleInEdge+1	
			elif(chosedEdge==4):
				aspersor.centerX,currentCenterY = updateCenterInHeight(2,axes,firstCircleInEdge,radioC,currentCenterY)
				aspersor.centerY = currentCenterY
				aspersor.draw()
				if firstCircleInEdge==aspersoresAltura:
					drawIn_Edges=False
					update = True
					input('')
					
				else:
					firstCircleInEdge = firstCircleInEdge+1

		else: #draw in a random place
			#aspersor = Circle(radioC,campo.maxX-radioC,campo.maxY-radioC,campo.minX+radioC,campo.minY+radioC)
			#aspersor.draw()
			numberIterations = numberIterations+1;
			drawIn_Edges = False
			chosedEdge = 1
			firstCircleInEdge = 1
			currentCenterX = 0
			currentCenterY = 0
			indexAxis = 0
			auxAxes = axes
			aspersoresBase,aspersoresAltura,axes = updateAllNewVariables(radioC,auxAxes,numberIterations,x,y)
			print(axes)
			update = False
			DrawedRectangles=DrawedRectangles+1
			print('\n%d Rectangulos dibujados de %d\n'%(DrawedRectangles,numRectangulos))
			if DrawedRectangles==numRectangulos-1:
				lastCircles(axes,aspersor,numRectangulos)
				DrawedRectangles=DrawedRectangles+1


		aspersores.append(aspersor)
		print("Aspersor %d, origen(%d,%d), area=%d"%(AspersoresDibujados+1,aspersor.centerX,aspersor.centerY,aspersor.area))
		AspersoresDibujados = AspersoresDibujados+1
	#print(aspersores)

	print("\n\n")
	opcion = int(input('0-Salir 1-Nuevos datos: '))
	if(opcion==1):
		tt.clearscreen()


