from random import choice


class artificial():
    '''Função para, em breve, criar o bot(ainda será trabalhada)'''
    def __init__(self, tela, cor):
        self.telaobj = tela
        self.cor = cor
        self.lista_op = []

    def getoplist(self):
        lista = self.telaobj.lista
        return lista

    def escolha(self):
        opt = {}
        lista = self.getoplist()
        print('a')
        for item in lista:
            if self.cor in item:
                opt[item] = lista[item]
