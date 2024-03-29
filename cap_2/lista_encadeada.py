'''
class Carro:
    def __init__(self, cor, preco, ano):
        self.cor = cor
        self.preco = preco
        self.ano = ano

    def pintura(self, cor):
        self.cor = cor
    def aumento_preco(self, percentual):
        self.preco = self.preco + ((self.preco * percentual)/100)

celta = Carro('preto', 1000, 1999)
ferrari = Carro('vermelho', 10000, 2000) 
'''        

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

            
     
            
            
            
            
  
                                
lista = ListaEncadeada()
lista.append(5)
lista.append(80)
lista.append(1)        
lista.append(4)        
#print(lista)
# lista.delete(1)
#print(lista)
lista.sort_asc()
print(lista)
            
        
