import PySimpleGUI as sg


class rank():
    '''Tela do ranking local'''
    def __init__(self):
        registro = self.importar()
        layout = [[sg.Frame('', [[sg.Text('Top 10 jogadores',font=('Consolas', 20, 'bold'),
                                          text_color='#6b8a66', background_color='#b1bf82')]],
                            element_justification='c', border_width=0, background_color='#b1bf82')
                   ]]
        cont = 1
        layout += [[sg.Text('Nome/ Jogos/ Vitorias/ Derrotas', background_color='#b1bf82',
                    font='Consolas 10')]]
        for c in range(len(registro)):
            if cont > 10:
                break
            nome = registro[c][0]
            pessoa = registro[c][1]
            frame = [[sg.Text(str(cont)+'° '+nome+':', background_color='#6b8a66'
                              ,size=(10, 1), font='Consolas 12'),
                     sg.Text(str(pessoa[0])+'/'+str(pessoa[1])+'/'+str(pessoa[2])+''
                             ,background_color='#6b8a66', size=(5, 1))]]
            layout += [[sg.Frame('', frame, size=(15, 1), background_color='#6b8a66')]]
            cont += 1
        layout += [[sg.Button('Voltar', key='ranking_voltar', enable_events=True,
                    size=(10, 1), button_color='#6b8a66')]]
        window = sg.Window('',
                    [[sg.Frame('',layout,element_justification='ce',background_color='#b1bf82')]],
                    size=(300, 520),element_justification='ce', background_color='#b1bf82')
        self.window = window
        self.main()

    def importar(self):
        jogadores = {}
        with open('armazenamento/jogadores.txt', 'r') as arq:
            linhas = arq.readlines()[2::]
        for linha in linhas:
            linha = linha.split(', ')
            nome = linha[0].replace('    ', '').capitalize()
            jogos = int(linha[1])
            vitorias = int(linha[2])
            empates = int(linha[3])
            derrotas = jogos - vitorias - empates
            jogadores[nome] = [jogos, vitorias, empates, derrotas]
        jogadores = sorted(jogadores.items(), key=lambda e: e[1][1], reverse=True)
        return jogadores

    def main(self):
        window = self.window
        while True:
            evento, valores = window.read()
            if evento == None:
                window.close()
                return False
            if evento == 'ranking_voltar':
                window.close()
                return True
            else:
                return False

