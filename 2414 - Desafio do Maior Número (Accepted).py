i =0
temp=0
vetor = list(map(int, input().split()))
x=len(vetor)
for i in range (0, x, 1):
    if (vetor[i]!=0):
       if (vetor[i]>=temp):
            temp=vetor[i]
    else:
        break
print(temp)