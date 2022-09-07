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

    return sg.Window('Tela inicial',layout,size=(200, 150))

def telaLista():
    sg.theme('Dark Green')
    layout = [
        [sg.Listbox(pa.listaNomePoder(),select_mode='extended',size=(30, 6))],
        [sg.Button('Comentar'),sg.Button('Voltar')]
    ]

    return sg.Window('Tela lista',layout)

def telaPoder():
    poder = pa.pegaPoder()
    sg.theme('Dark Green')
    layout = [
        [sg.Text('Seu poder é:',text_color='white')],
        [sg.Text(str(poder["nome"])+"!!!",text_color='white')],
        [sg.Text('O que seu poder faz? simples!',text_color='white')],
        [sg.Text('Seu poder é:',text_color='white')],
        [sg.Text(str(poder["desc"]),text_color='white')],
        [sg.Text('Legal né?',text_color='white')],
        [sg.Text('Aproveite seu poder!!!',text_color='white')],
        [sg.Button('Comentar'),sg.Button('Voltar')]
    ]
    return sg.Window('Tela poder',layout)

def telaComment(poder):
    sg.theme('Dark Green')
    comentarios = cm.showComment(poder["nome"])
    lista = list()
    for i in sorted(comentarios):
        lista.append("usuário: "+ str(i["nome"]) + " poder: "+ str(i["poder"])+ "\n"+ str(i["data"]) + "\n"+str(i["comment"]))
    layout =[
        [sg.Text('Poder: '+ str(poder["nome"]),text_color='white')],
        [sg.Text(str(poder["desc"]),text_color='white')],
        [sg.Listbox(lista,select_mode='extended',size=(30, 6))],
        [sg.Button('Voltar')]
    ]

def Menu():
    
