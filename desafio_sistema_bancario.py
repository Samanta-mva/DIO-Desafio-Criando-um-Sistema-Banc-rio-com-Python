# DESAFIO SISTEMA BANCARIO
"""
1) Separa o código por funções: 
    - Sacar / Depositar / Extrato / Sair

2) Criar pelo menos duas funções:
    - Criar cliente(usuario)
    - Criar conta corrente vinculada ao cliente(usuario)

    (FEITO)
1.a) Função saque com argumentos apenas por nome(keyword only) exemplo: nome='Samanta'
    Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques
    Sugestão de retorno: saldo e extrato

    (FEITO)
1.b) Função deposito com argumento apenas por posição(positional only) exemplo: Samanta
    Sugestão de argumentos: saldo, valor, extrato
    Sugestão de retorno: saldo e extrato

1.c) Função extrato argumentos por posição e por nome(positional only e keyword only)
    Argumento positional: saldo
    Argumento keyword: extrato

2.a) Função criar usuario deve armazenar os usuarios em uma lista, sendo composto por: nome, data de nascimento, CPF e endereço
    O endereço será uma string com: logradouro, número, bairro, cidade/UF
    O CPF deverá conter apenas números, sem pontos ou letras, não podendo ser cadastrado 2 usuarios com o mesmo CPF

2.b) Função criar conta corrente deve ser armazenado em uma lista, sendo composta por: agência, número da conta e usuário
    Número da conta é sequencial começando em 1
    Agência deve ser fixo '0001'
    O usuário pode ter mais de uma conta, mas cada conta só pode pertencer a um usuário

DICA → Para vincular uma conta a um usuário, filtre a lista de usuários, buscando o número do CPF informado para cada usuário da lista

Sinta-se livre para incrementar o sistema com novas funcionalidades e funções além das pedidas para o desafio.
"""

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\nOperação realizada com sucesso!\nVocê sacou R$ {valor:.2f}\n")

    else:
        print("Operação falhou! O valor informado é inválido.")


def depositar(saldo, valor, extrato,/):   
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"\nOperação realizada com sucesso!\nVocê depositou R$ {valor:.2f}\n")

    else:
        print("Operação falhou! O valor informado é inválido.")


def visualizar_extrato(saldo, /, *, extrato):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

→ """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        sacar(saldo=saldo,valor=valor,extrato=extrato,limite=limite,
              numero_saques=numero_saques,limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
         visualizar_extrato(saldo,extrato=extrato)        

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")