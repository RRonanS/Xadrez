class jogador():
    '''Classe do jogador, responsável por exibir o rank, ler e armazenar seus dados'''
    def __init__(self, nome):
        qnt_vitorias = 0
        qnt_jogos = 0
        qnt_empates = 0
        self.qnt_vitorias = qnt_vitorias
        self.qnt_jogos = qnt_jogos
        self.qnt_empates = qnt_empates
        self.nome = nome
        jogador.importar(self)

    def vitoria(self):
        vitorias = self.qnt_vitorias
        jogos = self.qnt_jogos
        vitorias += 1
        jogos += 1
        self.qnt_vitorias = vitorias
        self.qnt_jogos = jogos

    def empate(self):
        empates = self.qnt_empates
        jogos = self.qnt_jogos
        jogos += 1
        empates += 1
        self.qnt_empates = empates
        self.qnt_jogos = jogos

    def derrota(self):
        jogos = self.qnt_jogos
        jogos += 1
        self.qnt_jogos = jogos

    def importar(self):
        nome = self.nome
        achou = False
        linha = ''
        with open('armazenamento/jogadores.txt', 'r') as arquivo:
            linhas = arquivo.readlines()[1::]
            cont = 0
            for item in linhas:
                if nome in item:
                    print('[Sistema] Encontrado')
                    achou = True
                    linha = item
                    break
                cont += 1
        if not achou:
            print('[Sistema] Não encontrado')
        else:
            linha = linha.split(', ')
            jogos = int(linha[1])
            vitorias = int(linha[2])
            empates = int(linha[3])
            self.qnt_jogos = jogos
            self.qnt_vitorias = vitorias
            self.qnt_empates = empates
            self.linha_do_jogador = cont
            print('[Sistema] importou com sucesso')

    def exportar(self):
        nome = self.nome
        vitorias = str(self.qnt_vitorias)
        jogos = str(self.qnt_jogos)
        empates = str(self.qnt_empates)
        linhas = []
        if nome != '--OrderToDelete--':
            linha_jogador = '    ' + nome + ', ' + jogos + ', ' + vitorias + ', ' + empates
        else: linha_jogador = ''
        colocou = False
        with open('armazenamento/jogadores.txt', 'r') as arquivo:
            linhas = arquivo.readlines()[2::]
        cont = 0
        for x in linhas:
            x = x.replace('\n', '')
            if nome in x:
                linhas[cont] = linha_jogador
                colocou = True
            else: linhas[cont] = x
            cont += 1
        if not colocou: linhas.append(linha_jogador)
        with open('armazenamento/jogadores.txt', 'w') as arq:
            arq.write('Jogadores:\n')
            arq.write('    Nome, jogos, vitorias , empates\n')
            for item in linhas:
                if item != '':
                    arq.write(item+'\n')
        print('[Sistema] exportou com sucesso')

    def resetar(self):
        self.qnt_jogos = 0
        self.qnt_vitorias = 0
        self.qnt_empates = 0
        jogador.exportar(self)

    def deletar(self):
        self.nome = '--OrderToDelete--'
        jogador.exportar(self)

