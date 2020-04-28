nome = input()
fixo = float(input())
vendas = float(input())
comissao = 0.15 * vendas
fixo += comissao
print("TOTAL = R$ %0.2f" %fixo)
