from math import sqrt
from codigos.SystemIa import artificial as Ia

'''
    Durante os comentarios são falados alguns termos, aqui estão seus significados práticos
    # PySimpleGUI
        Se trata de uma biblioteca utilizada na criação de interfaces
    # Gráfico
        Um elemento do PySimpleGUI, que é basicamente uma lousa, onde você pode 
        adicionar, remover e manipular elementos geométricos e objetos da tela
    # Matriz
        Nossa matriz utilizada se trata de uma matriz 8x8 porém esta é tratada como linear
        ou seja, seus membros são números de 0 a 64 que remetem as casas do xadrez 
'''


class tela():
    # Init, gera o grafico e a tela, os exportanto pela classe
    def __init__(self):
        import PySimpleGUI as Sg
        # O tkinter é necessário para evitar bugs na hora de criar um executável
        # do programa, no entanto ele não é chamado em nenhum momento
        import tkinter
        width, height = 640, 640
        grafico = Sg.Graph((width, height), (0, 0), (width, height), enable_events=True,
                           background_color='black')
        janela = Sg.Window('Xadrez', [[grafico]], finalize=True,
                           background_color='white', size=(width + 30, 30 + height))
        self.directorio = 'arquivos/'
        self.tamanhos = (width, height)
        self.janela = janela
        self.grafico = grafico
        self.lista = []
        self.end = (False, '')
        self.bk_pos = 61
        self.wk_pos = 5
        self.pecaspretas = 16
        self.pecasbrancas = 16
        self.contador = 1
        self.casas = []
        self.matriz = {}
        self.pecas = {}

    # Gera as casas no grafico e a lista de casas
    def gerar_pontos(self):
        casas = []
        tamanhos = self.tamanhos
        grafico = self.grafico
        width, height = tamanhos[0], tamanhos[1]
        colunas = 8
        linhas = 8
        largura = (width // colunas)
        altura = (height // linhas)

        # Função que desenha os quadrados(casas) na tela
        def gerar_linha(h, cores):
            contador = self.contador
            for c in range(0, linhas):
                if c % 2 == 0:
                    cor = cores[0]
                else:
                    cor = cores[1]
                grafico.draw_rectangle((largura * c, h),
                                       ((largura * (c + 1)), h - altura),
                                       fill_color=cor,
                                       line_width=0)
                casa = [[(largura * c, h), ((largura * (c + 1)), h - altura)], contador, cor]
                casas.append(casa)
                contador += 1
                self.contador = contador

        cont = 0
        for c in range(height, 0, -altura):
            if cont == 8: break
            if cont % 2 == 0:
                cores = ['#bbbe64', '#eaf0ce']
            else:
                cores = ['#eaf0ce', '#bbbe64']
            gerar_linha(c, cores)
            cont += 1
        self.casas = casas
        # Criadas as casas, é gerada uma lista casas com seus valores
        # (numero, coordenada, cor, etc)

    # Cria os números e a matriz dos pontos, adiciona as peças no tabuleiro
    def criar_pontos(self, numeros=False):
        grafico = self.grafico
        casas = self.casas
        directorio = self.directorio
        cont = 1
        matriz = {}
        pecas = {}

        # Função auxiliar, ela é utilizada para criar peças cujo processo pode ser repetido
        # Funcinalmente, ou seja, serve apenas alguns tipos de peças
        def aux(c, nome):
            c = str(c)
            ind = nome + ' ' + str(contb)
            matriz[c].append(ind)
            matriz[c][2] = True
            item = matriz[c]
            pecas[ind] = grafico.draw_image(filename=directorio + nome + '.png',
                                            location=(item[0][0] - 40, item[0][1] + 40))

        # Desenho dos números nas casas caso o parâmetro da função seja True
        for item in casas:
            posicoes = item[0]
            tl = posicoes[0]
            dr = posicoes[1]
            mid = ((tl[0] + dr[0]) // 2, (tl[1] + dr[1]) // 2)
            if numeros:
                grafico.draw_text(text=str(cont), location=mid,
                                  color='red', font='bold')
            cor = item[2]
            matriz[str(cont)] = [mid, cor, False]
            cont += 1
        contb = contp = 0
        # Desenhos das peças dado os valores das casas
        for c in range(len(matriz) + 1):
            # Rei branco
            if c == 5:
                aux(c, 'whiteking')
            # Rainha branca
            if c == 4:
                aux(c, 'whitequeen')
            # Peoes brancos
            if c in range(9, 17):
                c = str(c)
                ind = 'whitepawn ' + str(contb)
                matriz[c].append(ind)
                matriz[c][2] = True
                item = matriz[c]
                pecas[ind] = grafico.draw_image(filename=directorio + 'whitepawn.png',
                                                location=(item[0][0] - 40, item[0][1] + 40))
                contb += 1
            # Torres brancas
            elif c == 1 or c == 8:
                valor = 1
                if c == 8: valor = 2
                c = str(c)
                ind = 'whiterook ' + str(valor)
                matriz[c].append(ind)
                matriz[c][2] = True
                item = matriz[c]
                pecas[ind] = grafico.draw_image(filename=directorio + 'whiterook.png',
                                                location=(item[0][0] - 40, item[0][1] + 40))
            # Cavalos brancos
            elif c == 2 or c == 7:
                valor = 1
                if c == 7: valor = 2
                c = str(c)
                ind = 'whiteknight ' + str(valor)
                matriz[c].append(ind)
                matriz[c][2] = True
                item = matriz[c]
                pecas[ind] = grafico.draw_image(filename=directorio + 'whiteknight.png',
                                                location=(item[0][0] - 40, item[0][1] + 40))
            # Rei preto
            if c == 61:
                aux(c, 'blackking')
            # Rainha preta
            if c == 60:
                aux(c, 'blackqueen')
            # Cavalos pretos
            elif c == 58 or c == 63:
                valor = 1
                if c == 63: valor = 2
                c = str(c)
                ind = 'blackknight ' + str(valor)
                matriz[c].append(ind)
                matriz[c][2] = True
                item = matriz[c]
                pecas[ind] = grafico.draw_image(filename=directorio + 'blackknight.png',
                                                location=(item[0][0] - 40, item[0][1] + 40))
            # Torres pretas
            elif c == 57 or c == 64:
                valor = 1
                if c == 64: valor = 2
                c = str(c)
                ind = 'blackrook ' + str(valor)
                matriz[c].append(ind)
                matriz[c][2] = True
                item = matriz[c]
                pecas[ind] = grafico.draw_image(filename=directorio + 'blackrook.png',
                                                location=(item[0][0] - 40, item[0][1] + 40))
            # Bispos brancos
            elif c == 3 or c == 6:
                valor = 1
                if c == 6: valor = 2
                c = str(c)
                ind = 'whitebishop ' + str(valor)
                matriz[c].append(ind)
                matriz[c][2] = True
                item = matriz[c]
                pecas[ind] = grafico.draw_image(filename=directorio + 'whitebishop.png',
                                                location=(item[0][0] - 40, item[0][1] + 40))
            # bispos pretos
            elif c == 59 or c == 62:
                valor = 1
                if c == 62: valor = 2
                c = str(c)
                ind = 'blackbishop ' + str(valor)
                matriz[c].append(ind)
                matriz[c][2] = True
                item = matriz[c]
                pecas[ind] = grafico.draw_image(filename=directorio + 'blackbishop.png',
                                                location=(item[0][0] - 40, item[0][1] + 40))
            # Peoes pretos
            elif c in range(49, 57):
                c = str(c)
                ind = 'blackpawn ' + str(contp)
                matriz[c].append(ind)
                matriz[c][2] = True
                item = matriz[c]
                pecas[ind] = grafico.draw_image(filename=directorio + 'blackpawn.png',
                                                location=(item[0][0] - 40, item[0][1] + 40))
                contp += 1
        self.matriz = matriz
        self.pecas = pecas
        # Gera dois registros, um com a matriz das casas
        # (Mostra dados de cada casa e se há peça nela)
        # e outro com os números do Pysimplegui de cada peça(Necessario para deletar e mover elas)

    # Retorna o centro da casa, passadas coordenadas dentro da mesma
    def mid_por_local(self, location):
        casas = self.casas
        x = location[0]
        y = location[1]
        for item in casas:
            pos = item[0]
            x_range = (pos[0][0], pos[1][0])
            y_range = (pos[0][1], pos[1][1])
            if x in range(x_range[0], x_range[1]) and y in range(y_range[1], y_range[0]):
                v1 = (x_range[0] + x_range[1]) // 2
                v2 = (y_range[0] + y_range[1]) // 2
                return (v1, v2)

    # Função auxiliar de outras funções de mesmo prefixo, fazendo basicamente
    # uma consulta na matriz
    def encontrar(self, location, tipo):
        mid = self.mid_por_local(location)
        if mid != None:
            matriz = self.matriz
            for c in range(1, len(matriz) + 1):
                item = matriz[str(c)]
                if item[0] == mid:
                    if tipo == 2:
                        return c
                    elif tipo == 1:
                        return matriz[str(c)][1]
                    elif tipo == 3 and matriz[str(c)][2]:
                        return matriz[str(c)][3]

    # Dada a posição retorna o número da casa na matriz
    def encontrar_num(self, location):
        valor = self.encontrar(location, 2)
        return valor

    # Dada a posição retorna a cor da casa
    def encontrar_cor(self, location):
        valor = self.encontrar(location, 1)
        return valor

    # Dada a posição retorna o nome da peça na casa ou null
    def encontrar_nome(self, location):
        valor = self.encontrar(location, 3)
        return valor

    # Dado o num, diz o nome da peça na casa
    def encontrar_nome_por_num(self, num):
        matriz = self.matriz
        try:
            item = matriz[str(num)][3]
        except:
            item = None
        return item

    # Dada posição inicial e final, move uma peça
    def mover_peca(self, inicial, final):
        nome = self.encontrar_nome(inicial)
        grafico = self.grafico
        pecas = self.pecas
        mid_i = self.mid_por_local(inicial)
        mid_f = self.mid_por_local(final)
        pos_i = (mid_i[0] - 40, mid_i[1] + 40)
        pos_f = (mid_f[0] - 40, mid_f[1] + 40)
        grafico.move_figure(pecas[nome], pos_f[0] - pos_i[0], pos_f[1] - pos_i[1])
        matriz = self.matriz
        num = str(self.encontrar_num(inicial))
        num_final = str(self.encontrar_num(final))
        matriz[num].pop(3)
        matriz[num][2] = False
        try:
            a = matriz[num_final][3]
            matriz[num_final][3] = nome
        except:
            matriz[num_final].append(nome)
        matriz[num_final][2] = True

    # Para criar areola ao redor da casa clicada dada posição qualquer desta
    def pintar(self, location, lista):
        areolas = []
        # Parte antiga, pinta somente a casa escolhida
        casas = self.casas
        num = self.encontrar_num(location)
        pos = ((), ())
        for casa in casas:
            if num == casa[1]:
                pos = casa[0]
                break
        grafico = self.grafico
        areola = grafico.draw_rectangle(pos[0], pos[1],
                                        line_width=3,
                                        line_color='green',
                                        )
        areolas.append(areola)
        # Adaptacao para pintar todas casas possiveis de alcancar
        nome = self.encontrar_nome_por_num(num)
        try:
            opcoes = lista[nome]
            # Pintar cada casa nas opcoes
            for x in opcoes:
                # Pegar posicoes da casa
                for casa in casas:
                    if x == casa[1]:
                        pos = casa[0]
                        areola = grafico.draw_rectangle(pos[0], pos[1],
                                                        line_width=3,
                                                        line_color='yellow')
                        areolas.append(areola)
                        break
        except:
            pass
        return areolas

    # Função para deletar uma peça dada sua localização aproximada
    def deletar_peca(self, location):
        pretas = self.pecaspretas
        brancas = self.pecasbrancas
        grafico = self.grafico
        pecas = self.pecas
        nome = self.encontrar_nome(location)
        if nome.startswith('black'):
            pretas -= 1
        elif nome.startswith('white'):
            brancas -= 1
        grafico.delete_figure(pecas[nome])
        num = str(self.encontrar_num(location))
        matriz = self.matriz
        matriz[num][3] = ''
        print('[Sistema] pecas restantes:\n', 'Pretas:', pretas, 'brancas:', brancas)

    # Diz se tem uma peca a frente de outra peca(Verifica toda a coluna)
    def tem_peca_na_frente(self, num, num_f):
        matriz = self.matriz
        if num > num_f:
            maior = num
            menor = num_f
        else:
            maior = num_f
            menor = num
        for c in range(maior - 8, menor, -8):
            nome = ''
            try:
                nome = matriz[str(c)][3]
            except:
                pass
            if nome != '':
                return True
        return False

    # Diz se tem peça na lateral(Verifica toda a linha)
    def tem_peca_na_lateral(self, num, lateral, num_f):
        res = False
        valor = num
        if num > num_f:
            menor = num_f
            maior = num
        else:
            maior = num_f
            menor = num
        for c in range(menor + 1, maior):
            nome = ''
            if lateral == 'direita':
                valor += 1
            elif lateral == 'esquerda':
                valor -= 1
            matriz = self.matriz
            try:
                nome = matriz[str(valor)][3]
            except:
                pass
            if nome != '' and nome != None:
                return True
        return res

    # Diz se tem peça na diagonal(Verficia toda a diagonal até o num_f)
    def tem_peca_na_diagonal(self, num_i, num_f, diagonal):
        lugar = False
        resultado = False
        if num_f > num_i:
            cont = 8
        else:
            cont = -8
        c = num_i
        while True:
            if c != num_i:
                if diagonal == 'esquerda':
                    c -= 1
                elif diagonal == 'direita':
                    c += 1
            nome = self.encontrar_nome_por_num(c)
            if (nome is not None) and nome != '' and c != num_i:
                if c == num_f:
                    lugar = True
                resultado = True
                break
            c += cont
            if c >= num_f and num_f > num_i:
                break
            elif c <= num_f and num_f < num_i:
                break

            if c > 64 or c < 0: break
        nome = self.encontrar_nome_por_num(num_i)
        if (('bishop' in nome) or ('queen' in nome)) and lugar:
            resultado = False
        return resultado

    # Diz se um movimento é válido(retorna booleano)
    def condicoes_movimentos_b(self, pos_i, pos_f, nomepeca):
        num_i = self.encontrar_num(pos_i)
        num_f = self.encontrar_num(pos_f)

        # Dado o numero da casa, converte para matriz x y
        def num_para_matriz(num):
            coluna = 1
            while True:
                if num > 8:
                    num -= 8
                    coluna += 1
                else:
                    break
            return (coluna, num)

        xi, yi = num_para_matriz(num_i)
        xf, yf = num_para_matriz(num_f)
        # Peões
        if nomepeca == 'whitepawn' or nomepeca == 'blackpawn':
            # variavel pra encurtar o código
            num_1 = 1
            if nomepeca == 'whitepawn':
                num_1 = -1
            # Cond se refere ao pulo duplo no primeiro movimento
            c1 = ((xf + (num_1 * 2)) == xi) and yi == yf
            c2 = ((8 <= num_i <= 16 and nomepeca.startswith('white'))
                  or (48 <= num_i <= 56) and nomepeca.startswith('black'))
            cond = c1 and c2 and not self.tem_peca_na_frente(num_i + (-8 * num_1), num_f + (-8 * num_1))
            if ((((yi == yf) and ((xf + num_1) == xi))
                 and self.encontrar_nome_por_num(num_f) is None) or cond) \
                    and not self.tem_peca_na_frente(num_i, num_f):
                return True
            else:
                return False
        # Reis
        if nomepeca == 'whiteking' or nomepeca == 'blackking':
            if sqrt(((xi - xf) ** 2) + ((yi - yf) ** 2)) <= sqrt(2):
                return True
            else:
                return False
        # Cavalos
        if nomepeca == 'whiteknight' or nomepeca == 'blackknight':
            condicao_a = True
            condicao_b = True
            if abs(xi - xf) != 2 or abs(yi - yf) != 1:
                condicao_a = False
            if abs(xi - xf) != 1 or abs(yi - yf) != 2:
                condicao_b = False
            if condicao_a or condicao_b:
                return True
            else:
                return False
        # Torres
        if nomepeca == 'whiterook' or nomepeca == 'blackrook':
            nomepeca = nomepeca.replace('rook', '')
            cond = False
            if xi != xf and yi == yf:
                cond = self.tem_peca_na_frente(num_i, num_f)
            else:
                if yi > yf:
                    cond = self.tem_peca_na_lateral(num_i, 'esquerda', num_f)
                elif yi < yf:
                    cond = self.tem_peca_na_lateral(num_i, 'direita', num_f)
            if (xi == xf or yi == yf) and (xi != xf or yi != yf) and (not cond):
                return True
            else:
                return False
        # Bispos
        if nomepeca == 'whitebishop' or nomepeca == 'blackbishop':
            diag = ''
            if yi > yf:
                diag = 'esquerda'
            elif yi < yf:
                diag = 'direita'
            cond = not self.tem_peca_na_diagonal(num_i, num_f, diag)
            if abs(xi - xf) != 0 and abs(xi - xf) == abs(yi - yf) and cond:
                return True
            else:
                return False
        # Rainhas
        if nomepeca == 'whitequeen' or nomepeca == 'blackqueen':
            # Movimento de torre
            nomepeca = nomepeca.replace('queen', '')
            condt = False
            if xi != xf:
                condt = self.tem_peca_na_frente(num_i, num_f)
            else:
                if yi > yf:
                    condt = self.tem_peca_na_lateral(num_i, 'esquerda', num_f)
                elif yi < yf:
                    condt = self.tem_peca_na_lateral(num_i, 'direita', num_f)
            condicao_r = False
            # Movimento de bispo
            diag = ''
            if yi > yf:
                diag = 'esquerda'
            elif yi < yf:
                diag = 'direita'
            condb = not self.tem_peca_na_diagonal(num_i, num_f, diag)
            condicao_b = False

            if (xi == xf or yi == yf) and (xi != xf or yi != yf):
                condicao_r = True
            if abs(xi - xf) != 0 and abs(xi - xf) == abs(yi - yf):
                condicao_b = True
            if (condicao_r and not condt) or (condicao_b and condb):
                return True
            else:
                return False

    # Para o peao capturar uma peca
    def peao_comer(self, pos_i, pos_f):
        nome_i = self.encontrar_nome(pos_i).split()[0]
        nome_f = self.encontrar_nome(pos_f).split()[0]
        cor_i = nome_i.replace('pawn', '')
        cor_f = nome_f.replace('pawn', '')
        mov = False
        num_i = self.encontrar_num(pos_i)
        num_f = self.encontrar_num(pos_f)
        cond1 = ((num_f == num_i + 9) or (num_f == num_i + 7)) and cor_i == 'white'
        cond2 = ((num_f == num_i - 9) or (num_f == num_i - 7)) and cor_i == 'black'
        # Satisfazendo as condições come a peça
        if (cond1 or cond2) and not cor_f.startswith(cor_i):
            self.deletar_peca(pos_f)
            self.mover_peca(pos_i, pos_f)
            mov = True
        # Se chegou no final do tabuleiro
        if ((1 <= num_f <= 8) or (56 <= num_f <= 64)) and mov:
            print('[Sistema] chamando funcao de recolocacao peao')
            self.peao_chegou_fim(pos_f, cor_i)
        # Se capturou o rei
        if 'king' in nome_f and not cor_f.startswith(cor_i):
            if nome_f.startswith('black'):
                end = (True, 'brancas')
            else:
                end = (True, 'pretas')
            print('[Sistema] fim de jogo')
            self.end = end
        return mov

    # Para uma peca em geral capturar outra
    def geral_comer(self, pos_i, pos_f):
        mov = False
        end = self.end
        nome_i = self.encontrar_nome(pos_i)
        nome_f = self.encontrar_nome(pos_f)
        if nome_i.startswith('black'):
            cor_i = 'black'
        else:
            cor_i = 'white'
        if nome_f.startswith('black'):
            cor_f = 'black'
        else:
            cor_f = 'white'
        if cor_i != cor_f:
            self.deletar_peca(pos_f)
            self.mover_peca(pos_i, pos_f)
            if 'king' in nome_f:
                if nome_f.startswith('black'):
                    end = (True, 'brancas')
                else:
                    end = (True, 'pretas')
            self.end = end
            mov = True
        return mov

    # Caso um peão chegue a ultima casa
    def peao_chegou_fim(self, pos_f, cor):
        matriz = self.matriz
        pecas = self.pecas
        num = self.encontrar_num(pos_f)
        print('[Sistema] Gerando tela de upgrade do peao')
        import PySimpleGUI as sg
        layout = [[sg.Frame('', [[sg.Text('Casa de trocas',
                                          font='bold', text_color='red')]])],
                  [sg.Text('Por qual peça deseja trocar seu peão:')],
                  [sg.Button('Bispo', key='Bispo', enable_events=True)],
                  [sg.Button('Cavalo', key='Cavalo', enable_events=True)],
                  [sg.Button('Rainha', key='Rainha', enable_events=True)],
                  [sg.Button('Torre', key='Torre', enable_events=True)]
                  ]
        window = sg.Window('', [[sg.Frame('', layout)]])
        while True:
            evento, valores = window.read()
            if evento == None:
                pass
            else:
                self.deletar_peca(pos_f)
                grafico = self.grafico
                diretorio = self.directorio
                pos_f = self.mid_por_local(pos_f)
                posi = pos_f[0] - 40
                posj = pos_f[1] + 40
                nome = ''
                ind = ''
                if evento == 'Bispo':
                    nome = 'bishop'
                    ind = cor + nome + ' extra'
                    pecas[ind] = grafico.draw_image(filename=(diretorio + cor + nome + '.png')
                                                    , location=(posi, posj))
                elif evento == 'Cavalo':
                    nome = 'knight'
                    ind = cor + nome + ' extra'
                    pecas[ind] = grafico.draw_image((diretorio + cor + nome + '.png'),
                                                    location=(posi, posj))
                elif evento == 'Rainha':
                    nome = 'queen'
                    ind = cor + nome + ' extra'
                    pecas[ind] = grafico.draw_image((diretorio + cor + nome + '.png'),
                                                    location=(posi, posj))
                elif evento == 'Torre':
                    nome = 'rook'
                    ind = cor + nome + ' extra'
                    pecas[ind] = grafico.draw_image((diretorio + cor + nome + '.png'),
                                                    location=(posi, posj))
                matriz[str(num)][3] = ind
                if cor == 'black':
                    pretas = self.pecaspretas
                    pretas += 1
                elif cor == 'white':
                    brancas = self.pecasbrancas
                    brancas += 1
                break
        window.close()

    # Gera uma lista de peças e seus movimentos possiveis, retorna tal lista
    def gerar_lista(self):
        opcoes = {}
        matriz = self.matriz
        # Teoria: num = {x| x pertence aos reais, 1<=x<=64}
        # Para todos x em num, para todos y em num, verificar se y é uma opcao de
        # movimento de x, caso verdadeiro, opcoes[nome_de_x], que é uma lista, recebe y
        for c in range(1, 65):
            nome = ''
            item = matriz[str(c)]
            tem_peca = item[2]
            if tem_peca:
                ind = item[3]
                nome = ind.split()[0]
                pos = item[0]
                for d in range(1, 65):
                    if c == d:
                        pass
                    else:
                        nome_f = ''
                        item_f = matriz[str(d)]
                        pos_f = item_f[0]
                        tem_peca2 = item_f[2]
                        cond = True
                        if tem_peca2:
                            nome_f = item_f[3]
                            if nome.startswith('black') and nome_f.startswith('black'):
                                cond = False
                            elif nome.startswith('white') and nome_f.startswith('white'):
                                cond = False
                        valido = self.condicoes_movimentos_b(pos, pos_f, nome)
                        # Condpawn é uma condicao especial para o peao, para ver se ele pode
                        # Comer alguma peca em tal posicao
                        condpawn = ('pawn' in nome) and (((d == c + 9 or d == c + 7) and 'white' in nome)
                                                         or (d == c - 9 or d == c - 7) and 'black' in nome) and \
                                   matriz[str(d)][2]
                        if valido and cond or (condpawn and cond):
                            # Caso tudo seja validado, ele adiciona a posicao na lista de
                            # posicoes possiveis da peca
                            num_f = self.encontrar_num(pos_f)
                            try:
                                opcoes[ind].append(num_f)
                            except:
                                opcoes[ind] = [num_f]
        return opcoes

    # Mostra um texto na tela por um tempo em segundos
    def display(self, texto, tempo):
        tamanhos = self.tamanhos
        grafico = self.grafico
        meiodex = tamanhos[0] // 2
        texto = texto.split('\n')
        exibindo = [tempo]
        font_size = 30
        y = tamanhos[1] // 2 + font_size * len(texto)
        for item in texto:
            exiba = grafico.draw_text(text=item, location=(meiodex, y),
                                      font=('bold', font_size), color='red')
            exibindo.append(exiba)
            y -= font_size
        self.exibindo = exibindo

    # Apaga o que esta sendo mostrado na tela(caso haja)
    def display_delete(self):
        exibindo = self.exibindo
        grafico = self.grafico
        for item in exibindo[1::]:
            grafico.delete_figure(item)

    # Verifica se algum dos reis está em cheque
    def esta_em_cheque(self):
        lista = self.lista
        wk = self.wk_pos
        bk = self.bk_pos
        xeque = False
        nome = ''
        num = 0
        for item in lista:
            if (wk in lista[item]) or (bk in lista[item]):
                xeque = True
                if item.startswith('white'):
                    nome = 'black'
                else:
                    nome = 'white'
                for coisa in self.matriz:
                    try:
                        if item in self.matriz[coisa][3]:
                            num = self.encontrar_num(self.matriz[coisa][0])
                    except:
                        pass
                break
        return (xeque, nome, num)

    # Gera uma lista de que peças podem ser movidas para evitar xeque mate
    def xeque_opcoes(self, num):
        # Adicionar caso o responsavel do xeque seja bispo ou torre e eu puder por peça na frente
        lista = self.lista
        quais_mover = []
        nome = self.encontrar_nome_por_num(num)
        print(nome)
        tipo = ''
        avaliable = []
        alcance_ataque = lista[self.encontrar_nome_por_num(num)]
        if nome.startswith('black'):
            rei_pos = self.wk_pos
        elif nome.startswith('white'):
            rei_pos = self.bk_pos
        if rei_pos > num:
            maior = rei_pos
            menor = num
        else:
            maior = num
            menor = rei_pos
        cond = ((maior - menor) % 8 == 0) or ((maior - menor) <= 7)
        if 'rook' in nome or (('queen' in nome) and cond):
            tipo = 'rook'
        elif 'bishop' in nome or 'queen' in nome:
            tipo = 'bishop'

        if tipo == 'rook':
            if self.modulo(num, rei_pos) % 8 == 0:
                # Então estão na mesma coluna
                avaliable = [x for x in range(maior, menor, -8)]
            else:
                # Então estão na mesma linha
                avaliable = [x for x in range(maior, menor, -1)]
        if tipo == 'bishop':
            # Diagonal esquerda ou direita?
            coluna_rei = rei_pos % 8
            coluna_bispo = num % 8
            if coluna_rei > coluna_bispo:
                # direita
                avaliable = [x for x in range(maior, menor, -7)]
            else:
                # esquerda
                avaliable = [x for x in range(maior, menor, -9)]

        for item in lista:
            # Consigo capturar a peça do xeque
            if num in lista[item]:
                quais_mover.append(item)
            # Consigo obstruir o ameaçador
            for x in lista[item]:
                if x in avaliable:
                    quais_mover.append(item)
                    break
        # Tem de verificar se o rei pode sair tambem
        king = self.encontrar_nome_por_num(rei_pos)
        for x in lista[king]:
            if x not in alcance_ataque:
                quais_mover.append(king)
                break
        self.avaliable = avaliable
        return quais_mover

    # Retorna modulo(Distância entre duas casas) em num (Desconsidere)
    def modulo(self, num_1, num_2):
        if num_1 > num_2:
            maior = num_1
            menor = num_2
        else:
            maior = num_2
            menor = num_1
        return maior - menor

    # Função principal da classe, responsável por tudo
    def rodar_tela(self, jogo=(False, '')):
        # Imports e variaveis
        import time
        from random import choice
        import PySimpleGUI as sg

        inicial = time.time()
        self.gerar_pontos()
        self.criar_pontos()
        janela = self.janela
        grafico = self.grafico
        brancas = self.pecasbrancas
        pretas = self.pecaspretas
        turno = choice(['brancas', 'pretas'])
        num_turnos = 1
        final = time.time()
        res = '%.2f' % (final - inicial)
        print('[Sistema]', 'jogo iniciado em', res, 'segundos')
        self.display('Turno ' + str(num_turnos) + ' \nPeças ' + turno, 2)
        areolas = []

        # Laço da tela, onde são recebidos os eventos
        while True:
            for areola in areolas:
                grafico.delete_figure(areola)
            xeque = False
            xeque_mate = False
            quais_mover = []
            rei_xeque = resp_xeque = ''
            lista = self.gerar_lista()
            self.lista = lista
            # Condicoes de vitoria
            # Rei em xeque:
            test_xeque = self.esta_em_cheque()
            if test_xeque[0]:
                print('Xeque', test_xeque[1], test_xeque[2])
                xeque = True
                resp_xeque = test_xeque[2]
                rei_xeque = test_xeque[1]
                quais_mover = self.xeque_opcoes(resp_xeque)
                avaliable = self.avaliable
                print('avaliable', avaliable)
                print('quais mover', quais_mover)
                if resp_xeque == 0:
                    xeque = False
                lista_do_ameacador = lista[self.encontrar_nome_por_num(resp_xeque)]
                try:
                    lista_do_ameacador.remove(self.bk_pos)
                except:
                    pass
                try:
                    lista_do_ameacador.remove(self.wk_pos)
                except:
                    pass
            # Verificar se o xeque também é xeque mate
            if xeque:
                if turno == 'brancas' and rei_xeque == 'black':
                    xeque_mate = True
                elif turno == 'pretas' and rei_xeque == 'white':
                    xeque_mate = True
                if len(quais_mover) == 0:
                    xeque_mate = True
            # Rei capturado:
            end = self.end
            fim = end[0]
            if xeque_mate:
                from codigos.TelaCadastro import telacadastro
                if rei_xeque == 'white':
                    nome = 'branco'
                    vencedor = 'pretas'
                else:
                    nome = 'preto'
                    vencedor = brancas
                sg.Popup('Fim de jogo!\n', 'O rei', nome, 'recebeu xeque mate'
                         , text_color='black')
                print('[Sistema] fim de jogo, rei capturado')
                telacadastro(vencedor)
                break
            # Chama a tela para cadastrar a partida
            if fim:
                from TelaCadastro import telacadastro
                sg.Popup('Fim de jogo!\n', 'As peças', end[1], 'capturaram o rei inimigo'
                         , font='bold', text_color='black', background_color='blue')
                print('[Sistema] fim de jogo, rei capturado')
                telacadastro(end[1])
                break
            # Alguem ficou sem peças:
            if pretas == 0 or brancas == 0:
                if pretas == 0:
                    venceu = 'brancas'
                else:
                    venceu = 'pretas'
                print('[Sistema] fim de jogo, sem peças restantes')
                sg.Popup('Fim de jogo, as peças', venceu, 'venceram!')
                break
            # Fim das condicoes de vitoria

            # Parte para obrigar o jogador a mexer peças para evitar xeque mate
            if xeque:
                for item in lista:
                    if item.startswith(rei_xeque) and item in quais_mover:
                        nova_lista = []
                        # Mudar a lista pondo apenas opções que acabem com o xeque
                        for x in lista[item]:
                            if x in avaliable:
                                nova_lista.append(x)
                            if x == resp_xeque:
                                nova_lista.append(x)
                        # Caso o rei consiga fugir se movendo
                        if 'king' in item:
                            for pos in lista[item]:
                                if pos not in lista_do_ameacador:
                                    nova_lista.append(pos)
                            for z in nova_lista:
                                if z in lista_do_ameacador:
                                    nova_lista.remove(z)
                        lista[item] = nova_lista
                    elif item.startswith(rei_xeque) and item not in quais_mover:
                        # Impede movimento daqueles que não puderem evitar o mate
                        lista[item] = []
            moveu = False
            # Chamada da leitura da tela do pysimplegui
            evento, valores = janela.read(timeout=1000, timeout_key='timeout')
            try:
                IA = False
                nome = (self.encontrar_nome(valores[0]))
                cor = ''
                if nome.startswith('white'):
                    cor = 'brancas'
                    ing = 'white'
                elif nome.startswith('black'):
                    cor = 'pretas'
                    ing = 'black'
                # Adicionar a IA aqui(em breve)
                if jogo[0] and turno != jogo[1]:
                    IA = True
                    ia = Ia(self, ing)
                    escolha = ia.escolha()
                    if turno == 'brancas':
                        turno = 'pretas'
                    else:
                        turno = 'brancas'
                    num_turnos += 1
                    print('[Sistema] novo turno,', turno)

                # Essa parte aqui serve para mover peças
                pos_inicial = valores[0]
                if nome is not None and nome != '' and turno == cor \
                        and evento != 'timeout' and not IA:
                    areolas = self.pintar(pos_inicial, lista)
                    pos_final = janela.read()[1][0]
                    nome_final = self.encontrar_nome(pos_final)
                    cond = False
                    if self.encontrar_num(pos_final) in lista[nome]:
                        cond = True
                    # Caso a peca escolhida seja um peao, e haja uma peca no lugar
                    if 'pawn' in nome and not (nome_final is None or nome_final == ''):
                        moveu = self.peao_comer(pos_inicial, pos_final)

                    # Move uma peça sem ser peão e sem comer outra peça
                    elif (nome_final is None or nome_final == '') and cond:
                        self.mover_peca(pos_inicial, pos_final)
                        # Verifica se é um peão
                        if 'pawn' in nome:
                            # verifica a cor e se está numa casa de fim
                            if 'black' in nome:
                                if 0 <= self.encontrar_num(pos_final) <= 8:
                                    self.peao_chegou_fim(pos_final, 'black')
                            elif 'white' in nome:
                                if 56 <= self.encontrar_num(pos_final) <= 64:
                                    self.peao_chegou_fim(pos_final, 'white')
                        # Atualizar posição do rei
                        if 'king' in nome:
                            if 'black' in nome:
                                self.bk_pos = self.encontrar_num(pos_final)
                            elif 'white' in nome:
                                self.wk_pos = self.encontrar_num(pos_final)
                        moveu = True
                    # Move uma peça comendo outra na pos_final
                    elif (nome_final is not None and nome_final != '') and cond:
                        moveu = self.geral_comer(pos_inicial, pos_final)
                        # Atualizar posição do rei
                        if 'king' in nome:
                            if 'black' in nome:
                                self.bk_pos = self.encontrar_num(pos_final)
                            elif 'white' in nome:
                                self.wk_pos = self.encontrar_num(pos_final)
                    if moveu:
                        if turno == 'brancas':
                            turno = 'pretas'
                        else:
                            turno = 'brancas'
                        num_turnos += 1
                        print('[Sistema] novo turno,', turno)
                        self.display_delete()
                        self.display('Turno ' + str(num_turnos) + ' \nPeças ' + turno, 2)
                    for areola in areolas: grafico.delete_figure(areola)
                # Fim da parte de mover peças
            except:
                pass
            # Eventos extras, remove displays e fecha o app caso o usuario clique no xis
            if evento is None:
                break
            if evento == 'timeout':
                exibindo = self.exibindo
                exibindo[0] = exibindo[0] - 1
                self.display_delete()
        janela.close()
        import main


