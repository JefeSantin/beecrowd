NOTAS=0
VALOR = float(input())
print("NOTAS:")
valor_atual=VALOR
nota_atual=100.00
troca = "nota(s)"
while True:
    if nota_atual <= valor_atual:
        NOTAS+=1
        valor_atual -= nota_atual
    else:
        print("%d %s de R$ %5.2f" % (NOTAS,troca, nota_atual))
        if valor_atual == 0.00:
            break
        if nota_atual == 100:
            nota_atual = 50
        elif nota_atual == 50:
            nota_atual = 20
        elif nota_atual == 20:
            nota_atual = 10
        elif nota_atual == 10:
            nota_atual = 5
        elif nota_atual == 5:
            nota_atual = 2
        elif nota_atual == 2:
            print("MOEDAS:")
            troca="moeda(s)"
            nota_atual = 1.00
        elif nota_atual == 1.00:
            troca="moeda(s)"
            nota_atual = 0.50
        elif nota_atual == 0.50:
            nota_atual = 0.25
        elif nota_atual == 0.25:
            troca="moeda(s)"
            nota_atual = 0.10
        elif nota_atual == 0.10:
            troca="moeda(s)"
            nota_atual = 0.05
        elif nota_atual == 0.05:
            troca="moeda(s)"
            nota_atual = 0.01
        elif nota_atual == 0.01:
            troca="moeda(s)"
            nota_atual = 0.00
            break
        NOTAS = 0
