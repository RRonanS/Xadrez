import PySimpleGUI as sg


class telacadastro():
    '''Tela de cadastro de partidas'''
    def __init__(self, vencedor):
        nome1 = ''
        nome2 = ''
        layout = [[sg.Text('Deseja cadastrar essa partida?', font=('Consolas', 13),
                    background_color='#b1bf82')],
                  [sg.Text('Peças brancas:', font=('Consolas', 10)
                    ,background_color='#b1bf82'),
                  sg.Input('nome',key='nomeinput'
                    ,enable_events=True)], # NOME1
                  [sg.Text('Peças pretas:', font=('Consolas', 10)
                    ,background_color='#b1bf82'),
                  sg.Input('nome',key='nome2input'
                    ,enable_events=True)],   # NOME2
                  [sg.Button('Confirmar', key='submit',enable_events=True, button_color='#6b8a66'),
                   sg.Button('Cancelar', key='cancel', enable_events=True, button_color='#6b8a66')]]
        window = sg.Window('',layout,size=(300, 300), background_color= '#b1bf82')
        self.window = window
        self.nome1 = nome1
        self.nome2 = nome2
        self.vencedor = vencedor
        self.main()

    def cadastrar(self):
        nome1 = self.nome1
        nome2 = self.nome2
        vencedor = self.vencedor
        # Verificar se nomes sao validos
        valido = True
        if nome1 == nome2:
            valido = False
        if nome1.isnumeric() or nome2.isnumeric():
            valido = False
        if len(nome1) >= 12 or len(nome2) >= 12:
            valido = False
        if len(nome1) < 3 or len(nome2) < 3:
            valido = False
        if valido:
            from jogadores import jogador
            jogador1 = jogador(nome1)
            jogador2 = jogador(nome2)
            if vencedor == 'brancas':
                jogador1.vitoria()
                jogador2.derrota()
            elif vencedor == 'pretas':
                jogador2.vitoria()
                jogador1.derrota()
            elif vencedor == 'empate':
                jogador1.empate()
                jogador2.empate()
            jogador1.exportar()
            jogador2.exportar()
            return True
        else:
            return False

    def main(self):
        window = self.window
        while True:
            evento, valores = window.read()
            if evento == None:
                break
            elif evento == 'submit':
                self.nome1 = window.Element('nomeinput').get()
                self.nome2 = window.Element('nome2input').get()
                cadastrou = self.cadastrar()
                if cadastrou:
                    sg.Popup('Cadastrado com sucesso!')
                    break
                else:
                    sg.Popup('Ops, algo de errado aconteceu')
            elif evento == 'cancel':
                break
            elif 'nome' in evento:
                if evento == 'nomeinput':
                    entrada = valores['nomeinput'].replace('nome', '')
                    window.Element('nomeinput').update(entrada)
                elif evento == 'nome2input':
                    entrada = valores['nome2input'].replace('nome', '')
                    window.Element('nome2input').update(entrada)
