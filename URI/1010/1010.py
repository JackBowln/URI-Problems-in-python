x = input().split()

cod1 = float(x[0])
num1 = float(x[1])
preco1 = float(x[2])

y = input().split()

cod2 = float(y[0])
num2 = float(y[1])
preco2 = float(y[2])

valor = (num1 * preco1) + (num2 * preco2)
print("VALOR A PAGAR: R$ %0.2f"%valor)