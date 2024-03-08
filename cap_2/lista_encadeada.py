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
    
    def append(self, valor):

        if self.elemento == None:
            self.elemento = valor
            self.prox_elemento = ListaEncadeada()
            # print(valor)
            # print('valor_adicionado \n ')
        else:
            # print(self.elemento)
            self.prox_elemento.append(valor)
                        
    def busca(self, indice):
      
        lista = self
    
        for i in range(indice):
            lista = lista.prox_elemento            
        return lista.elemento

    def insert(self, valor, indice):
      
        lista = self
    
        for i in range(indice - 1):
            lista = lista.prox_elemento            
        prox_elemento_antigo = lista.prox_elemento
        lista.prox_elemento = ListaEncadeada()
        lista.prox_elemento.elemento = valor
        lista.prox_elemento.prox_elemento = prox_elemento_antigo

                     
# caso de teste           
lista = ListaEncadeada()
lista.append('AMANDA')
lista.append('MATHEUS')
lista.append('DEBORA')        
lista.append('PINGO')        
print(lista)  
            

# lista = Lista()
# lista.insert(5)
# lista.insert(4)
# lista.insert(3)
# printar lista 
        
        
