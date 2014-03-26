from fractions import Fraction
import csv

def readFile(filename = "datos.txt"):
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
	A=[Fraction(1) for x in range(n)]

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

#y(x) =  A0 = (x-x1)(x-x2)(x-x3)+
#		A1 (x-x0)(x-x2)(x-x3)+
#		A2 (x-x0)(x-x1)(x-x3)+
#		A3 (x-x0)(x-x1)(x-x2);

	
datos = readFile()
Lagrange(datos, 2)