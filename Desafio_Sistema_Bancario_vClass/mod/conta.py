from abc import ABC, abstractmethod
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\nOperação falhou!\nSaldo suficiente.")

        elif valor > 0:
            self._saldo -= valor
            print("\nSaque realizado com sucesso!")
            return True

        else:
            print("\nA operação falhou!\nO valor informado é inválido.")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\nDepósito realizado com sucesso!")
        else:
            print("\nA operação falhou!\nO valor informado é inválido.")
            return False

        return True
    
    def __str__(self):
        return f'''\
                Agência:{self._agencia}
                C/C:{self._numero}
                Titular:{self._cliente.nome}
                '''


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\nOperação falhou!\nO valor de saque excede o limite.")

        elif excedeu_saques:
            print("\nOperação falhou!\nNúmero máximo de saques excedido.")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    if clientes_filtrados:
        return clientes_filtrados[0]
    else:
        None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print('Este cliente não possui uma conta.')
        return
    
    return cliente.contas[0]


def extrato(clientes):
    cpf = input('Digite o CPF >> ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não registrado.')
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print(f'{'=' * 5} Extrato {'=' * 5}')
    transacoes = conta.historico.transacoes

    extrato = ''
    if not transacoes:
        extrato = 'A conta não possui movimentações.'
    else:
        for transacao in transacoes:
            extrato += f'\n{transacao['tipo']}: R${transacao['valor']:,.2f}'

    print(extrato)
    print(f'\nSaldo: R${conta.saldo:,.2f}')
    print('=' * 19)



def sacar(clientes):
    cpf = input('Digite o CPF >> ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\nCliente não encontrado!')
        return
    
    valor = float(input('Valor de SAQUE >> R$'))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)


def depositar(clientes):
    cpf = input('Digite o CPF >> ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\nCliente não encontrado!')
        return
    
    valor = float(input('Valor de DEPOSITO >> R$'))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)


def criar_conta(numeroConta, clientes, conta):
    cpf = input('Digite o CPF >> ')
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('\nCliente não registrado.')
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numeroConta)
    contas.append(conta)
    cliente.contas.append(conta)

    print('\nConta criada com sucesso!')


def listar_contas(contas):
    for conta in contas:
        print('=' * 20)
        print(conta)

    
def criar_cliente(clientes):
    cpf = input('Digite o CPF >> ')
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print('\nEste CPF já está vinculado a um cliente.')
        return
    
    nome = input('Nome completo:\n')
    data_nascimento = input('Data de Nascimento:\n')
    endereco = input('Endereço (logradouro, bairro, cidade/sigla estado):\n')

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print('\nCliente cadastrado com sucesso!')


clientes = []
contas = []
