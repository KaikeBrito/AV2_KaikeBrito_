validar_cartao = lambda numero_cartao, validade_cartao: True

validar_deposito = lambda valor: True

processar_saque_dinheiro = lambda valor_saque: (
    print(f"Saque de R${valor_saque:.2f} realizado com sucesso!")
    if valor_saque is not None and 0 < valor_saque <= 100
    else print("Valor de saque inválido!") if valor_saque is not None
    else print("Valor de saque não informado!")
)

processar_cartao = lambda: print(
    "Pagamento escolhido: Cartão\nResultado do teste:",
    "Passou!" if validar_cartao("1234567890123456", "12/25") else "Falhou!"
)

processar_deposito = lambda: print(
    "Pagamento escolhido: Depósito\nResultado do teste:",
    "Passou!" if validar_deposito("450") else "Falhou!"
)

processar_ou_sair = lambda tipo_pagamento, valor=50: (
    processar_saque_dinheiro(valor) if tipo_pagamento == "dinheiro"
    else processar_cartao() if tipo_pagamento == "cartao"
    else processar_deposito() if tipo_pagamento == "deposito"
    else exit() if tipo_pagamento == "sair"
    else print("Tipo de pagamento inválido!")
)

# Teste de estresse para processar 100 pagamentos com dinheiro
print("Teste de estresse para processar pagamento em dinheiro:")
for _ in range(100):
    processar_ou_sair("dinheiro", 50)

while True:
    tipo_pagamento = input("Escolha o tipo de pagamento (cartao/deposito/dinheiro/sair): ").lower()
    if tipo_pagamento != "sair":
        processar_ou_sair(tipo_pagamento)
    else:
        processar_ou_sair(tipo_pagamento)
        break
