# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

produto = input("digite o nome do produto: ")
preco = float(input("digite o preço do produto: "))
desconto = float(input("digite o desconto (%): "))

valor_desconto = preco * (desconto / 100)
preco_final = preco - valor_desconto

print("---resultado---")
print("produto: ", produto)
print("valor do desconto: R$", valor_desconto)
print("preço final com desconto: R$", preco_final)