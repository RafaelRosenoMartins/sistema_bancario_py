from banco.operacoes import Historico

class Conta:
    def __init__(self, numero, titular):
        self._numero = numero
        self._titular = titular
        self._saldo = 0.0
        self._historico = Historico()

    def get_saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._historico.adicionar_transacao("Deposito", valor)
            return True
        return False

    def sacar(self, valor):
        # Sera sobrescrito pelas subclasses
        pass

    def ver_extrato(self):
        print(f"Conta: {self._numero} | Titular: {self._titular}")
        self._historico.imprimir()
        print(f"Saldo Total: R$ {self._saldo:.2f}")

class ContaCorrente(Conta):
    def __init__(self, numero, titular, limite=500.0):
        super().__init__(numero, titular)
        self._limite = limite

    def sacar(self, valor):
        saldo_disponivel = self._saldo + self._limite
        if valor > 0 and valor <= saldo_disponivel:
            self._saldo -= valor
            self._historico.adicionar_transacao("Saque CC", valor)
            return True
        return False

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            self._historico.adicionar_transacao("Saque CP", valor)
            return True
        return False