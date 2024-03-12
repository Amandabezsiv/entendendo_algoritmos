class ListaEncadeada:
    def __init__(self):

        self.elemento = None
        self.prox_elemento = None

    def __repr__(self):
        
        
        if self.elemento == None:
            return '[]'
        else:
            elementos = ''    
            lista = self
            while lista.elemento != None:
                elementos += str(lista.elemento) + ', '
                lista = lista.prox_elemento
                
            return '[' + elementos[:-2] + ']'

    def __len__(self):
        lista = self
        _counter = 0

        while lista != None:
            lista = lista.prox_elemento
            _counter+=1

        return _counter-1

    def __getitem__(self, indice):
      
        lista = self

        for i in range(indice):
            lista = lista.prox_elemento
            if lista == None:
                raise IndexError(f'Índice {indice} maior que o tamanho da lista')
        if not lista.elemento:
                raise IndexError(f'Índice {indice} é maior que o tamanho da lista')
        return lista.elemento

    def search(self, indice):

        lista = self

        for i in range(indice):
            lista = lista.prox_elemento
            if lista == None:
                raise IndexError(f'Índice {indice} maior que o tamanho da lista')
        if not lista.elemento:
                raise IndexError(f'Índice {indice} é maior que o tamanho da lista')
        return lista
    
    def append(self, valor):

        if self.elemento == None:
            self.elemento = valor
            self.prox_elemento = ListaEncadeada()
        else:
            self.prox_elemento.append(valor)
                    

    def insert(self, valor, indice):
      
        lista = self.search(indice - 1)
              
        prox_elemento_antigo = lista.prox_elemento
        lista.prox_elemento = ListaEncadeada()
        lista.prox_elemento.elemento = valor
        lista.prox_elemento.prox_elemento = prox_elemento_antigo

    def delete(self, indice):

        if not indice:
            self.elemento = self.prox_elemento.elemento
            self.prox_elemento = self.prox_elemento.prox_elemento
        else:
            lista = self.search(indice - 1)
            lista.prox_elemento = lista.prox_elemento.prox_elemento
            if lista.prox_elemento == None:
                lista.prox_elemento = ListaEncadeada()

    def sort_asc(self):
        lista_ordenada = ListaEncadeada()

        lista = self.prox_elemento
        
        elemento = self.elemento

        while lista.elemento != None:
            ponteiro, indice_elemento = 1, 0
            while lista.elemento != None:
                if elemento > lista.elemento:
                    elemento = lista.elemento
                    indice_elemento = ponteiro
                    
                lista = lista.prox_elemento
                ponteiro+=1

            lista_ordenada.append(elemento)

            self.delete(indice_elemento)

            elemento = self.elemento
            lista = self.prox_elemento

        lista_ordenada.append(elemento)
        
        self.elemento = lista_ordenada.elemento
        self.prox_elemento = lista_ordenada.prox_elemento

# pilha com push e pop
class Pilha:
    def __init__(self):
        self.lista_encadeada = ListaEncadeada()
        self.ultimo_indice = -1
        
    def __repr__(self):
        return str(self.lista_encadeada)

    def push(self, valor):
        self.lista_encadeada.append(valor)
        self.ultimo_indice += 1

    def pop(self):
        self.lista_encadeada.delete(self.ultimo_indice)
        self.ultimo_indice -= 1
        

pilha = Pilha()
pilha.push(1)
pilha.push(2)
print(pilha)
pilha.pop()
print(pilha)
pilha.pop()
print(pilha)
