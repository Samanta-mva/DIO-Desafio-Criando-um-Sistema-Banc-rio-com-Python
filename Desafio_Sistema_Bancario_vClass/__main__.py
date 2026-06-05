from mod.conta import *

def main():

    while True:
        menu =    '''
            [1] Sacar
            [2] Depositar
            [3] Exibir Extrato
            [4] Novo Cliente
            [5] Nova Conta
            [6] Listar Contas
            [0] Sair

    Digite uma opção: '''

        opcao = int(input(menu))

        match opcao:
            case 1:
                sacar(clientes)
            case 2:
                depositar(clientes)
            case 3:
                extrato(clientes)
            case 4:
                criar_cliente(clientes)
            case 5:
                num_conta = len(contas) + 1
                criar_conta(numeroConta=num_conta, clientes=clientes, conta=contas)
            case 6:
                listar_contas(contas)
            case 0:
                print('\nObrigado por ser nosso cliente.\nVolte sempre!\n')
                break

if __name__ == '__main__':
    main()