"""FATURAMENTO DO MELHOR E DO PIOR MÊS DO ANO"""

meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
vendas_1sem = [2500, 29000, 17780, 15870, 19900, 22200]
vendas_2sem = [19850, 20120, 17549, 15555, 49051, 9650]

vendas_1sem.extend(vendas_2sem)
maior_valor = max(vendas_1sem)
menor_valor = min(vendas_1sem)
print(menor_valor)
print(maior_valor)


i_maior_valor = vendas_1sem.index(maior_valor)
i_menor_valor = vendas_1sem.index(menor_valor)

print('O melhor valor do ano foi {} com venda de {}'.format(meses[i_maior_valor],maior_valor))
print('O menor valor do ano foi {} com vendas de {}'.format(meses[i_menor_valor], menor_valor))