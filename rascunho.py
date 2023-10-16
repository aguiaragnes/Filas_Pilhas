class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Pilha:
    def __init__(self):
        self.topo = None

    def push(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.topo
        self.topo = novo_no

    def pop(self):
        if self.is_empty():
            return None
        valor = self.topo.valor
        self.topo = self.topo.proximo
        return valor

    def __str__(self):
        if self.is_empty():
            return "Pilha vazia"
        no_atual = self.topo
        resultado = ""
        while no_atual:
            resultado += str(no_atual.valor) + "\n"
            no_atual = no_atual.proximo
        return resultado

    def is_empty(self):
        return not bool(self.topo)_