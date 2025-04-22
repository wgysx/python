produto = input("Digite o nome do produto: ")

valor_produto = float(input("Digite o valor do produto: R$ "))


valor_pago = float(input("Digite o valor pago pelo cliente: R$ "))

troco = valor_pago - valor_produto


print("\n------------------------------------")
print("Comprovante de Venda")
print("------------------------------------")
print(f"Produto: {produto}")
print(f"Valor do Produto: R$ {valor_produto:.2f}")
print(f"Valor Pago: R$ {valor_pago:.2f}")
print(f"Troco: R$ {troco:.2f}")
print("------------------------------------")
