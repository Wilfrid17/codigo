"""ALTERAÇÃO INCREMENTAI DE VARIAVEIS
"""
faturamento = 3000
faturamento += 1000

lista = ['mac', 'iphone']
vendas = [100, 200]
#Para adicionar ipad na lista ultilizamos lista vai recebe ele mesmo mas outra lista ou lista.append
lista = lista + ['ipad']

print(lista)
print(vendas)



soma_vendas = 300
#para adicinar na soma a quantidade de ipad 
soma_vendas += 500
print(soma_vendas)

email = 'Esse mês vendemos um total de {} produto, sendo :\n{} unidade de .\n {} unidade de {}'.format(soma_vendas, vendas[0], lista[0], vendas[1], lista[1])
#adicionar no final do texto o Ipad

email +=  '\n{} unidade de Ipad'.format(500)
print(email)

