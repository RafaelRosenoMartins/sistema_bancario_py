class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.lista_contas = []

    def registrar_conta(self, conta):
        self.lista_contas.append(conta)

    def localizar_conta(self, numero):
        for c in self.lista_contas:
            if c._numero == numero:
                return c
        return None