from banco.contas import ContaCorrente, ContaPoupanca
from banco.sistema import Banco

def executar_sistema():
    meu_banco = Banco("Banco Central")
    
    while True:
        print(f"\n--- {meu_banco.nome} ---")
        print("1. Abrir Conta Corrente")
        print("2. Abrir Conta Poupanca")
        print("3. Deposito")
        print("4. Saque")
        print("5. Extrato")
        print("0. Sair")
        
        opcao = input("Selecione: ")

        if opcao == "1" or opcao == "2":
            num = input("Numero da conta: ")
            nome = input("Titular: ")
            if opcao == "1":
                nova = ContaCorrente(num, nome)
            else:
                nova = ContaPoupanca(num, nome)
            meu_banco.registrar_conta(nova)
            print("Conta registrada.")

        elif opcao == "3":
            num = input("Numero da conta: ")
            c = meu_banco.localizar_conta(num)
            if c:
                v = float(input("Valor do deposito: "))
                if c.depositar(v):
                    print("Sucesso.")
                else:
                    print("Valor invalido.")
            else:
                print("Erro: Conta nao existe.")

        elif opcao == "4":
            num = input("Numero da conta: ")
            c = meu_banco.localizar_conta(num)
            if c:
                v = float(input("Valor do saque: "))
                if c.sacar(v):
                    print("Saque ok.")
                else:
                    print("Saldo insuficiente.")
            else:
                print("Erro: Conta nao existe.")

        elif opcao == "5":
            num = input("Numero da conta: ")
            c = meu_banco.localizar_conta(num)
            if c:
                c.ver_extrato()
            else:
                print("Erro: Conta nao existe.")

        elif opcao == "0":
            print("Sistema encerrado.")
            break
        else:
            print("Opcao invalida.")

if __name__ == "__main__":
    executar_sistema()