from datetime import datetime

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, tipo, valor):
        agora = datetime.now()
        data_formatada = agora.strftime("%d/%m/%Y %H:%M")
        registro = f"{data_formatada} - {tipo}: R$ {valor:.2f}"
        self.transacoes.append(registro)

    def imprimir(self):
        print("\n--- Historico de Operacoes ---")
        if not self.transacoes:
            print("Nenhuma transacao realizada.")
        else:
            for t in self.transacoes:
                print(t)