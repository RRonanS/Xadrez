class menu():
    '''Classe responsável pelo menu do jogo'''
    def __init__(self):
        from codigos import info
        import PySimpleGUI as Sg

        layout = [[Sg.Text('Xadrez Mania', key='title', text_color='#6b8a66',
                           font=('Courier New', 22, 'bold'), background_color='#b1bf82')],
                  [Sg.Button(visible=False)],
                  [Sg.Button('1 jogador', key='pve', size=(11, 1), font='Consolas 12',
                             button_color='#6b8a66', border_width=0)],
                  [Sg.Button('2 jogadores', key='pvp', size=(11, 1), font='Consolas 12',
                             button_color='#6b8a66', border_width=0)],
                  [Sg.Button('Rank', key='rank', size=(11, 1), font='Consolas 12',
                             button_color='#6b8a66', border_width=0)],
                  [Sg.Button('Info', key='info', size=(11, 1), font='Consolas 12',
                             button_color='#6b8a66', border_width=0)],
                  [Sg.Text('', background_color='#b1bf82')],
                  [Sg.Text('', background_color='#b1bf82')],
                  [Sg.Text('', background_color='#b1bf82')],
                  [Sg.Text('', background_color='#b1bf82')],
                  [Sg.Text(info.version)]]

        info_layout = [[Sg.Text('Informações', text_color='#6b8a66', justification='center',
                                font=('Courier New', 22, 'bold'), background_color='#b1bf82')],
                       [Sg.Text('Devs:', font=('Consolas', 13, 'bold'), background_color='#b1bf82')]]
        for dev in info.devs:
            info_layout += [[Sg.Text('- ' + dev[0] + ' ' + dev[1], font=('Consolas', 12, 'italic'),
                                     text_color='#586b58', background_color='#b1bf82')]]

        info_layout += [[Sg.Text('Ultima atualização: ' + info.last_update, font=('Consolas', 10)
                                 , background_color='#b1bf82')]]
        info_layout += [[Sg.Button('Voltar', key='info_fechar', size=(8, 1), font='Consolas 10',
                                   button_color='#6b8a66', border_width=0)]]

        layout_final = [[Sg.Column(layout, size=(250, 250),
                                   element_justification='center', key='main', background_color='#b1bf82'),
                         Sg.Column(info_layout, visible=False,
                                   key='info_layout', size=(250, 250), background_color='#b1bf82')]]

        tela = Sg.Window('Menu', layout_final,
                         size=(250, 250), background_color='#b1bf82')
        self.tela = tela

    def animacao(self, cont):
        tela = self.tela
        frase = 'Xadrez Mania'
        if cont == 12:
            tela.Element('title').update('Xadrez Mania')
        else:
            if cont == 1 or cont == 8:
                frase = frase.upper()
            elif cont == 2 or cont == 9:
                frase = frase.lower()
            else:
                frase = list(frase)
                frase[cont] = frase[cont].capitalize()
                frase = ''.join(frase)
            tela.Element('title').update(frase)