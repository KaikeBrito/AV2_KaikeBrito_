contas_corrente = {
    "usuario1": {"saldo": 1500.00, "senha": "senha1"},
    "usuario2": {"saldo": 3000.00, "senha": "senha2"},
    "usuario3": {"saldo": 500.00, "senha": "senha3"},
}

atualizar_saldo = lambda id_usuario, valor: contas_corrente[id_usuario].update({"saldo": contas_corrente[id_usuario]["saldo"] + valor})

processar_saque = lambda id_usuario, valor_saque: (
    print(f"Saque de R${valor_saque:.2f} realizado com sucesso!")
    if contas_corrente[id_usuario]["saldo"] >= valor_saque
    and (atualizar_saldo(id_usuario, -valor_saque), True)
    else print("Saldo insuficiente para o saque!")
) or print(f"Saldo atual: R${contas_corrente[id_usuario]['saldo']:.2f}")

processar_pagamento_cartao = lambda: (
    lambda numero_cartao=None, validade_cartao=None, valor_pago=None: (
        print(f"Pagamento aprovado com R${valor_pago}!")
        if (
            numero_cartao := input("Digite o número do cartão de crédito: ")
        )
        and (
            validade_cartao := input(
                "Digite a data de validade do cartão (MM/AA): "
            )
        )
        and (valor_pago := float(input("Digite o valor pago com cartão: ")))
        and validar_cartao(numero_cartao, validade_cartao)
        else print("Pagamento recusado!")
    )
)()

processar_deposito = lambda: (
    lambda id_usuario=None, valor=None: (
        (
            lambda saldo_atualizado: print(f"Depósito de R${valor:.2f} efetuado com sucesso!\nSaldo atual: R${saldo_atualizado:.2f}")
        )(atualizar_saldo(id_usuario, valor) or contas_corrente[id_usuario]["saldo"])
        if valor <= contas_corrente[id_usuario]["saldo"]
        else print("Valor de depósito excede o saldo disponível!")
    )
)(
    input("Digite o ID/login do usuário: "),
    float(input("Digite o valor do depósito: ")),
)

detalhes_deposito_bancario = lambda banco, agencia, conta, valor: print(
    f"Depósito bancário de R${valor:.2f} realizado com sucesso.\nDetalhes do depósito:\nBanco: {banco}\nAgência: {agencia}\nConta: {conta}"
)

validar_cartao = (
    lambda numero_cartao, validade_cartao: True
)

while True:
    login_usuario = lambda: input("Digite o ID/login do usuário: ")
    senha_usuario = lambda: input("Digite a senha do usuário: ")

    if (
        (id_usuario := login_usuario()) in contas_corrente
        and contas_corrente[id_usuario]["senha"] == senha_usuario()
    ):
        print("Login efetuado com sucesso.")
        while True:
            tipo_transacao = input("Escolha o tipo de transação (saque/cartao/deposito/sair): ").lower()

            if tipo_transacao == "sair":
                break

            if tipo_transacao == "saque":
                valor_saque = float(input("Digite o valor do saque em conta corrente: "))
                processar_saque(id_usuario, valor_saque)
            elif tipo_transacao == "cartao":
                processar_pagamento_cartao()
            elif tipo_transacao == "deposito":
                processar_deposito()
            else:
                print("Opção de transação inválida. Por favor, escolha entre 'saque', 'cartao', 'deposito' ou 'sair'.")

    else:
        print("ID/login ou senha incorretos. Tente novamente.")
