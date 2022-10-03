import math


a = input()
float(a)
b = input()
float(b)
c = input()
float(c)
x1 = 0
x2 = 0

delta = b ** 2 - (4 * a * c)
print("%.5f" % (delta))

if (x1 <= 0 or x2 <= 0):
    raise("Deu Raiz negativa")
elif x1 == 0 or x2 == 0:
        print("Impossivel calcular")
x1 = b*(-1) + (math.sqrt(delta))
x1 = x1 / (2 * a) 
print("%.5f" % (x1))
x2 = b*(-1) - (math.sqrt(delta)) 
x2 = x2 / (2 * a)
print("%.5f" % (x2))
    