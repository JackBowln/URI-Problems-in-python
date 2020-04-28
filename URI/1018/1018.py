n = int(input())
print(n)
cedulas = [100, 50, 20, 10, 5, 2, 1]
for cedula in cedulas:
    qtd_cedulas = int(n / cedula)
    print("{} nota(s) de R$ {},00".format(qtd_cedulas, cedula))
    n -= qtd_cedulas * cedula
