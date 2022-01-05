from codigos import menu
import PySimpleGUI as Sg
import tkinter


def leitura():
	menu_tela = menu.menu()
	menu_window = menu_tela.tela
	cont = 1
	actual_window = menu_window
	while True:
		evento, valores = actual_window.read(timeout=500)
		if evento == None: break
		elif evento == 'pvp':
			menu_window.close()
			from codigos.tela import tela
			try:
				game = tela()
				game.rodar_tela()
				break
			except:
				pass
		elif evento == 'pve':
			Sg.Popup('Em breve.', button_color='#6b8a66', background_color='#b1bf82', line_width=10)
		elif evento == 'info':
			menu_window.Element('info_layout').update(visible=True)
			menu_window.Element('main').update(visible=False)
		elif evento == 'info_fechar':
			menu_window.Element('info_layout').update(visible=False)
			menu_window.Element('main').update(visible=True)
		elif evento == 'rank':
			from codigos.TelaRanking import rank
			actual_window.close()
			if rank():
				leitura()
				break
			else:
				actual_window.close()
				menu_window.close()
				break

		menu_tela.animacao(cont)
		cont += 1
		if cont > 12:
			cont = 1
	actual_window.close()


leitura()
