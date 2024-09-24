SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
OTHERS = 19849.53

total =  sum([SP, RJ, MG, ES, OTHERS])

print(f"Total = {total}")
for estate, value in zip(("SP", "RJ", "MG", "ES", "Outros"), (SP, RJ, MG, ES, OTHERS)):
    print(f"{estate} = {(value/total)*100:.2f}% de representação")
