import math
a = int(input("valor de a:"))
b = int(input("valor de b:"))
x1 = (a**b) / (b+4)
x2 = (b**a) / (a+32)
x = x1/x2 
print(x)

raiz = math.sqrt(x)
print(raiz)
n = raiz * math.pi
print(n)

