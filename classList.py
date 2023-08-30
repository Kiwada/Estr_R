class ListaZ:
 def __init__(self):
      self.itens = []
      self.n = 0

def EstaVazia(self):
    return self.n == 0

def mostar(self):
    i = 0 
    while i < self.n:
        print(self.items[i])
        i += 1


def mostra2(self):
     for item in self.itens:
        print(item)


def esvaziar(self):
    i = 0 
    while i < self.n:
        self.itens.pop(i)
        i += 1