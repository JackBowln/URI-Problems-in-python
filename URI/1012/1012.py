x = input().split()
a = float(x[0])
b = float(x[1])
c = float(x[2])
tri = (a*c)/2
pi = 3.14159
circ = pi * (c**2)
trap = ((a + b)*c)/2
quad = b**2
ret = a*b
print("TRIANGULO: %0.3f" %tri)
print("CIRCULO: %0.3f" %circ)
print("TRAPEZIO: %0.3f" %trap)
print("QUADRADO: %0.3f" %quad)
print("RETANGULO: %0.3f" %ret)
