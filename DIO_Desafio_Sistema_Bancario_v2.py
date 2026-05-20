# Desafio final DIO curso de Python

from random import randint, choice
from time import sleep
from datetime import datetime


def menu_primario():
    data = ''
    hora = ''
    def criar_usuario(usuario):
        print(f"""\n{'=' * 30}
{'Cadastro de Clientes':^30}
{'=' * 30}

É um prazer ter você com a gente. 
Seu cadastro é o primeiro passo para 
uma experiência bancária simples, 
segura e feita para facilitar o seu 
dia a dia. Aqui, seu dinheiro trabalha 
com você — e não o contrário
                """)

        print('Preencha corretamente com os seus dados')

        while True:
            num_cpf = int(input('\nCPF somente números: ').strip())
            cpf = str(num_cpf)

            if len(cpf) == 11:
                break

            elif num_cpf in usuario:
                print('O portador deste CPF já é nosso cliente.')
                return

            else:
                print('\nVerifique o número digitado!')

        nome = input('Nome completo: ').strip()

        while True:
            nascimento = str(input('Nascimento DD/MM/AAAA: ')).strip()
            if len(nascimento) < 10:
                print('\nAlgo deu errado, digite novamente!\nExemplo: 30/12/1999.')
            else:
                break

        endereco = [input('Logradouro: ').strip(),
                    input('nº ').strip(),
                    input('Complemento: ').strip(),
                    input('Bairro: ').strip(),
                    input('Cidade: ').strip(),
                    input('Estado(UF): ').strip()]

        usuarios[num_cpf] = {
            'nome': nome,
            'contas': [],
            'nascimento': nascimento,
            'endereco': endereco
        }

        print('\nCliente cadastrado com sucesso!\n')
        print('Agora confirme seus dados para criamos uma conta.\n')
        criar_conta(AGENCIA, ID_CONTA, usuarios)


    def criar_conta(ag, contas, usuario):
        num_cpf = int(input('\nInforme seu CPF (apenas números): ').strip())

        if num_cpf not in usuario:
            print('CPF não cadastrado.')
            while True:
                cadastrar = str(input('\nDeseja se tornar nosso cliente? [S/N]')).upper().strip().split()
                if cadastrar[0] not in 'NS':
                    print('Digite apenas "S" para Sim ou "N" para Não.')
                elif cadastrar[0] == 'S':
                    criar_usuario(usuario)
                elif cadastrar[0] == 'N':
                    return None


        letras = 'A','B','C'
        senha_gerada = str(randint(0,99)) + choice(letras) + str(randint(22,73))
        print(type(contas), contas)
        conta = {
            'agencia': ag,
            'numero_conta': len(contas) + 1,
            'senha': senha_gerada,
            'saldo': 0.0,
            'extrato': {f'{data}':[],},
            'saques': 0
        }

        usuario[num_cpf]['contas'].append(conta)
        sleep(2)
        print('=' * 30)
        print(f'{"\nAnote os dados de acesso da \nsua nova conta no banco MÜLLER!":^30}')
        print('=' * 30)
        sleep(1)
        dados = f"""
        Dados da Conta:
        Nome {usuario[num_cpf]['nome']}
        Agencia {conta['agencia']}
        Conta {conta['numero_conta']}
        Senha {conta['senha']}

        """
        print(dados)
        contas.append(len(contas) + 1)
        return contas


    def acessar_conta(cad_usuario):
        def depositar(saldo, extrato):
            data = datetime.now().strftime("%d-%m-%Y")
            hora = datetime.now().strftime("%H:%M:%S")

            if len(extrato.get(data, [])) == 10:
                print('Limite de transações diárias atingido. Volte amanhã!\n')
                sleep(3)
                return saldo, extrato
                
            else:
                while True:
                    try:
                        valor = float(input('Qual valor você deseja DEPOSITAR?\n→ R$ ').strip())
                        if valor > 0:
                            saldo += valor                        
                            extrato.setdefault(data, []).append(f'{hora} >> Depósito: R$ {valor:.2f}')
                            print(f'Operação realizada com sucesso!\nVocê depositou R$ {valor:.2f}')

                        else:
                            print('Valor inválido!\nDigite um valor acima de 0.')

                    except ValueError:
                        print('Erro!\nDigite novamente.')

                    return saldo, extrato

        def sacar(*, saldo, extrato, numero_saques, limite_saques):
            data = datetime.now().strftime("%d-%m-%Y")
            hora = datetime.now().strftime("%H:%M:%S")

            if len(extrato.get(data, [])) == 10:
                print('Limite de transações diárias atingido. Volte amanhã!')
                return saldo, extrato, numero_saques
            else:
                try:
                    valor = float(input('Qual valor você deseja SACAR?\n→ R$ ').strip())

                    if numero_saques >= limite_saques:
                        print('Operação inválida!\nVocê já atingiu o limite de saques.')

                    elif valor > saldo:
                        print('Operação inválida!\nSaldo da conta insuficiente.')

                    elif valor > 0:
                        saldo -= valor
                        extrato[f'{data}'].append(f'{hora} << Saque: R$ {valor:.2f}')
                        numero_saques += 1
                        print(f'\nOperação realizada com sucesso!\nVocê sacou R$ {valor:.2f}')

                except ValueError:
                    print('\nValor inválido!\nDigite um valor acima de 0.')

                else:
                    return saldo, extrato, numero_saques

        def visualizar_extrato(saldo, /, *, extrato):
            if not extrato:
                print('\nNão há registro de operações!')
            else:
                print(f'{'=' * 30}\n{'EXTRATO':^30}\n{'=' * 30}')

                for dia in extrato:
                    for transacao in extrato[dia]:
                        print(dia, transacao)

        def transacao_diaria(data, extrato):
            maxTransacaoes = 10
            contTransacoes = 0
            for dia in extrato:
                if dia == data:
                    contTransacoes += 1
            if contTransacoes == maxTransacaoes:
                print('Você excedeu o limite de transações diárias. Volte amanhã!\n')            
            else:
                pass
        
        def menu_conta(cad_usuarios, cpf_conta, num_conta):
            sleep(1)
            menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair

    Digite sua opção:
    → """

            usuario = None

            for conta in cad_usuarios[cpf_conta]['contas']:
                if conta['numero_conta'] == num_conta:
                    usuario = conta
                    break

            if usuario is None:
                print(f'Conta {num_conta} não encontrada para este CPF.')
                return

            saldo = usuario['saldo']
            extrato = usuario['extrato']
            numero_saques = usuario['saques']
            LIMITE_SAQUES = 3

            while True:
                print(f"""\n{'=' * 30}
Conta {usuario['numero_conta']}
    Saldo atual R$ {saldo:.2f}
    Saques realizados {numero_saques}    
{'=' * 30}""")
                try:
                    opcao = int(input(menu).strip())

                    if opcao == 1:
                        saldo, extrato = depositar(saldo, extrato)

                    elif opcao == 2:
                        saldo, extrato, numero_saques = sacar(
                            saldo=saldo, extrato=extrato,
                            numero_saques=numero_saques,
                            limite_saques=LIMITE_SAQUES)

                    elif opcao == 3:
                         visualizar_extrato(saldo, extrato=extrato)

                    elif opcao == 0:
                        usuario['saldo'] = saldo
                        usuario['extrato'] = extrato
                        usuario['saques'] = numero_saques
                        break

                    else:
                        print('\nOpção inválida! Digite 1, 2, 3 ou 0 para uma opção válida.')

                except ValueError:
                    print('\nErro! Digite apenas números.')

        sleep(1)
        print(f"""
{'=' * 30}
{'Acessando a Conta':^30}
{'=' * 30}
""")

        try:
            cpf = int(input('Digite seu CPF (somente números): ').strip())
        except ValueError:
            print('\nCPF inválido!')
            return

        if cpf not in cad_usuario:
            print('\nCPF não cadastrado.\nVerifique os digitos e tente novamente!\n')
            return

        usuario = cad_usuario[cpf]

        try:
            conta = int(input('Digite o número da conta: ').strip())
        except ValueError:
            print('\nNúmero de conta inválido!')
            return

        senha = input('Digite a senha: ').upper().strip()

        if any(c['numero_conta'] == conta and c['senha'] == senha for c in usuario['contas']):
            print('\nAcessando a conta...')
            menu_conta(cad_usuario,cpf,conta)

        else:
            print('\nConta ou senha não correspondem!')





    usuarios = {}
    AGENCIA = '0001'
    ID_CONTA = []

    sleep(1)
    menu_principal = f"""{'=' * 30}
{'Bem Vindo ao banco':^30}
{'MÜLLER':^30}
{'=' * 30}

    [1] Acessar Conta
    [2] Nova Conta para Clientes
    [3] Ainda Não é Cliente
    [0] Sair
    
    Digite sua opção: 
    → """


    while True:
        try:
            opcao = int(input(menu_principal).strip())

            if opcao == 1:
                acessar_conta(usuarios)
            elif opcao == 2:
                ID_CONTA = criar_conta(ag=AGENCIA, contas=ID_CONTA, usuario=usuarios)
            elif opcao == 3:
                criar_usuario(usuarios)
            elif opcao == 0: break

        except ValueError:
            print('\nDigite uma opção válida!')


menu_primario()

