cod_peca1, num_peca1, valor_unit1 = map(float, input().split())

cod_peca2, num_peca2, valor_unit2 = map(float, input().split())

valor_total = (num_peca1 * valor_unit1) + (num_peca2 * valor_unit2)

print("VALOR A PAGAR: R$ {:.2f}".format(valor_total))
