idade = 1
soma = 0 
quantidade = 0


while idade >= 0:
    idade = int(input())
    if idade >=0:
        soma = soma + idade
        quantidade +=1
media=(soma / quantidade)
print("{:.2f}".format(media))