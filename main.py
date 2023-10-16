class No:

    def __init__(self, carga=0, anterior=0):
        self.carga = carga
        self.anterior = anterior

    def __repr__(self):
        return '%s -> %s' % (self.carga, self.anterior)


class Pilha:

    def __init__(self):
        self.topo = None

    def push(self, carga):
        novo = No(carga)
        novo.proximo = self.topo
        self.topo = novo

    def pop(self):
        if self.is_empty():
            return None
        carga = self.topo.carga
        self.topo = self.topo.proximo
        return carga

    def __str__(self):
        if self.is_empty():
            return 'Pilha vazia'
        atual = self.topo
        resultado = ''
        while atual:
            resultado += str(atual.carga) + '\n'
            atual = atual.proximo
        return resultado

    def is_empty(self):
        return self.topo is None

