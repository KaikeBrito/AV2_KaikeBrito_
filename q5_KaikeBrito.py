from flask import Flask, request, render_template, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

app = Flask(__name__)

contas_corrente = {
    "usuario1": {"saldo": 1500.00, "senha": generate_password_hash("senha1")},
    "usuario2": {"saldo": 3000.00, "senha": generate_password_hash("senha2")},
    "usuario3": {"saldo": 500.00, "senha": generate_password_hash("senha3")},
}

encrypt_data = lambda data, key: (
    (cipher := AES.new(key, AES.MODE_CBC)),
    (ciphertext := cipher.encrypt(pad(data.encode(), AES.block_size))),
    cipher.iv
)

decrypt_data = lambda ciphertext, key, iv: (
    cipher := AES.new(key, AES.MODE_CBC, iv),
    unpad(cipher.decrypt(ciphertext), AES.block_size).decode()
)

validar_login = lambda login, senha: (
    check_password_hash(contas_corrente[login]["senha"], senha)
    if login in contas_corrente
    else False
)

validar_cartao = lambda numero_cartao, validade_cartao: True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    login = request.form.get("login")
    senha = request.form.get("senha")
    if validar_login(login, senha):
        return redirect(url_for("realizar_transacao"))
    else:
        return "Login ou senha incorretos. Tente novamente."

@app.route("/realizar-transacao", methods=["GET", "POST"])
def realizar_transacao():
    if request.method == "GET":
        return render_template("transacao.html")
    elif request.method == "POST":
        operacao = request.form.get("operacao")
        id_usuario = request.form.get("id_usuario")
        valor = float(request.form.get("valor"))

        if operacao == "saque":
            processar_saque(id_usuario, valor)
        elif operacao == "deposito":
            processar_deposito(id_usuario, valor)
        elif operacao == "cartao":
            processar_pagamento_cartao(valor)

        return redirect(url_for("realizar_transacao"))

processar_saque = lambda id_usuario, valor_saque: (
    print(f"Saque de R${valor_saque:.2f} realizado com sucesso!")
    if contas_corrente[id_usuario]["saldo"] >= valor_saque
    and (atualizar_saldo(id_usuario, -valor_saque), True)
    else print("Saldo insuficiente para o saque!")
) or print(f"Saldo atual: R${contas_corrente[id_usuario]['saldo']:.2f}")

processar_deposito = lambda id_usuario, valor: (
    (lambda saldo_atualizado: print(f"Depósito de R${valor:.2f} efetuado com sucesso!\nSaldo atual: R${saldo_atualizado:.2f}")
    if saldo_atualizado is not None
    else print("Valor de depósito excede o saldo disponível!") if valor > 0
    else print("Valor de depósito inválido!"))(contas_corrente[id_usuario]["saldo"] + valor)
)

processar_pagamento_cartao = lambda valor_pago: (
    print(f"Pagamento aprovado com R${valor_pago:.2f}!")
    if (
        (numero_cartao := input("Digite o número do cartão de crédito: "))
        and (validade_cartao := input("Digite a data de validade do cartão (MM/AA): "))
        and validar_cartao(numero_cartao, validade_cartao)
    )
    else print("Pagamento recusado!")
)

atualizar_saldo = lambda id_usuario, valor: contas_corrente[id_usuario].update({"saldo": contas_corrente[id_usuario]["saldo"] + valor})


if __name__ == "__main__":
    app.run(debug=True)
