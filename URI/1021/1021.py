n = float(input())

cedulas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for cedula in cedulas:
    qtd_cedulas = int(n / cedula)
    print("{} nota(s) de R$ {:.2f}".format(qtd_cedulas, cedula))
    n -= qtd_cedulas * cedula

print("MOEDAS:")
for moeda in moedas:
    qtd_moedas = int(round(n,2) / moeda)
    print("{} moeda(s) de R$ {:.2f}".format(qtd_moedas, moeda))
    n -= qtd_moedas * moeda