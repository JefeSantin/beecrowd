import math

valores = input().split()

ttl_placas = int(valores[0]) * int(valores[1])

resultado = []

for i in range(1, 10):
  um_porcento = i / 10
  qtd_placas = ttl_placas * um_porcento
  qtd_placas_str = str(math.ceil(qtd_placas))
  resultado.append(qtd_placas_str)
  
resultado_str = " ".join(resultado)

print(resultado_str)