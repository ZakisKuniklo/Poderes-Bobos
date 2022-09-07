#menu
from PySimpleGUI import PySimpleGUI as sg
import poderaleatorio as pa
import comment as cm

def telaInicial():
    sg.theme('Dark Green')
    layout = [
        [sg.Text('Poderes bobos!!!',text_color='white')],
        [sg.Button('Listar Poderes')],
        [sg.Button('Ganhar Poder')],
        [sg.Button('Sair')]
    ]

    janela = sg.Window('Tela inicial',layout,size=(200, 150))

    while True:
        eventos, valores = janela.read()
        if eventos == sg.WINDOW_CLOSED or eventos == 'Sair':
            break

telaInicial()