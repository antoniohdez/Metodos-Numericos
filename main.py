from fractions import Fraction
import csv

def readFile(filename = "newton.txt"):
	with open(filename,'r') as file:
		try:
			reader = csv.reader(file)
			n = int(next(reader)[0])
			datos = [[0 for x in range(2)] for x in range(n)]
			x = y = 0
			print("{:10} {:10}".format("X","Y"))
			for row in reader:
				for val in row:
					datos[x][y] = int(val)
					print("{:10}".format(val), end=" ")
					y += 1
				print("")
				x += 1
				y = 0

		except csv.Error as e:
			sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
	return datos

def Lagrange(datos, valor):
	n =	len(datos)
	A=[1 for x in range(n)]
	for x in range(n):
		divisor = 1
		for xi in range(n):
			if xi != x:
				divisor *= datos[x][0] - datos[xi][0]
		A[x] = Fraction(datos[x][1])/Fraction(divisor)

	resultado = 0
	for x in range(n):
		multi = 1
		for xi in range(n):
			if xi != x:
				multi *= valor - datos[xi][0]
		resultado += A[x] * Fraction(multi)	
	
	print()
	print("El valor interpolado de Y para el valor X = {} es: {}".format(valor, resultado))
	return resultado

def Newton(datos, valor, orden):
	n =	len(datos)
	resultado = 0
	diferencia = datos[1][0] - datos[0][0]
	for x in range(1, n):	
		if diferencia != (datos[x][0] - datos[x-1][0]):
			return Lagrange(datos, valor)

	if orden >= n:
		return Lagrange(datos, valor)
	deltaY = []
	for x in range(orden-1):
		deltaY.append( [0 for x in range(n-(x + 1))] )
		if x == 0:
			for xi in range(len(deltaY[0])):
				deltaY[0][xi] = datos[xi+1][1] - datos[xi][1]
				print(deltaY[0][xi], end=" ")
			print()
		else:
			for xi in range(len(deltaY[x])):
				deltaY[x][xi] = deltaY[x-1][xi+1] - deltaY[x-1][xi]
				print(deltaY[x][xi], end=" ")
			print()

	return resultado

	
datos = readFile()
#Lagrange(datos, 2)
Newton(datos, 3.2, 4)