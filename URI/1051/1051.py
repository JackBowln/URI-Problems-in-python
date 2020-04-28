renda = float(input())
imp1 = (renda - 2000)*0.08
imp2 = (1000*0.08) + (renda - 3000)*0.18
imp3 = (1000 * 0.08) + (1500 * 0.18) + (renda - 4500)*0.28

if renda < 2000:
    print("Isento")
elif 3000 > renda > 2000:
    print("R$ %0.2f" %imp1)
elif 4500 > renda > 3000:
    print("R$ %0.2f"%imp2)
else:
    print("R$ %0.2f"%imp3)