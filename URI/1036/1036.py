x = input().split()
A = float(x[0])
B = float(x[1])
C = float(x[2])
d = (B**2-(4*A*C))
print(A,"x² +",B,"y +",C)
if A == 0.0 or d < 0:
    print("Impossivel calcular")
else:
    R1 = (-B + d ** 0.5)/(2*A)
    R2 = (-B - d ** 0.5)/(2*A)
    print("R1 = ""{0:.5f}".format(R1, 5))
    print("R2 = ""{0:.5f}".format(R2, 5))