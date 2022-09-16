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
        [sg.Button('Adicionar novo Poder')],
        [sg.Button('Sair')]
    ]
    return sg.Window('Tela inicial',layout,size=(200, 175),finalize=True)

def telaLista():
    sg.theme('Dark Green')
    layout = [
        [sg.Listbox(pa.listaNomePoder(),select_mode='extended',size=(30, 6),key = 'ListaPoder')],
        [sg.Button('Comentar'),sg.Button('Voltar')]
    ]
    return sg.Window('Tela lista',layout,finalize=True)

def telaPoder(poder):
    sg.theme('Dark Green')
    layout = [
        [sg.Text('Seu poder é:',text_color='white')],
        [sg.Text(str(poder["nome"]),text_color='white')],
        [sg.Text('O que seu poder faz? simples!',text_color='white')],
        [sg.Text(str(poder["desc"]),text_color='white')],
        [sg.Text('Legal né?',text_color='white')],
        [sg.Text('Aproveite seu poder!!!',text_color='white')],
        [sg.Button('Comentar'),sg.Button('Voltar')]
    ]
    return sg.Window('Tela poder',layout,finalize=True)

def telaComment(poder):
    sg.theme('Dark Green')
    comentarios = cm.showComment(poder["nome"])
    lista = list()
    for i in sorted(comentarios):
        lista.append("usuário: "+ str(i["nome"]) + " poder: "+ str(i["poder"])+ "\n"+ str(i["data"]) + "\n"+str(i["comment"]))
    layout =[
        [sg.Text('Poder: '+ str(poder["nome"]),text_color='white')],
        [sg.Text(str(poder["desc"]),text_color='white')],
        [sg.Listbox(lista,select_mode='extended',size=(70, 6),horizontal_scroll=True)],
        [sg.Button('Voltar')]
    ]
    return sg.Window('Tela Comentários',layout,finalize=True)

def telaAddPoder():
    sg.theme('Dark Green')
    layout =[
        [sg.Text('Adicionar um novo poder:',text_color='white')],
        [sg.Text('Nome:      ',text_color='white'),sg.Input(key='nomePoder')],
        [sg.Text('Descrição:',text_color='white'),sg.Multiline(key='desc',size=(40,5))],
        [sg.Button('Adicionar'),sg.Button('Voltar')]
    ]
    return sg.Window('Tela novo poder',layout,finalize=True)

def telaPoderAdicionado():
    sg.theme('Dark Green')
    layout =[
        [sg.Text('Poder adicionado!',text_color='white')],
        [sg.Button('Voltar')]
    ]
    return sg.Window('Poder adicionado!',layout,finalize=True)

def menu():
    pa.criaArquivos(pa.file1)
    pa.criaArquivos(pa.file2)
    poderAtual = None
    janela1, janela2, janela3, janela4, janela5 ,janela6,janela7= telaInicial(),None,None,None,None,None,None
    janelaAtual = 0
    while True:
        window, event, values = sg.read_all_windows()
        if event== sg.WIN_CLOSED or event == 'Sair':
            if window is not janela6:
                break
        elif window == janela1 and event == 'Listar Poderes':
            janela2 = telaLista()
            janela1.hide()
        elif window == janela2 and event == 'Voltar':
            janela2.hide()
            janela1.un_hide()
        elif window == janela2 and event == 'Comentar':
            if values["ListaPoder"] is not None:
                poder = pa.buscaItem(pa.loadTable(pa.file1),"nome",values["ListaPoder"][0])
                janela4 = telaComment(poder[0])
                janelaAtual = 2
                janela2.hide()
        elif window == janela4 and event == 'Voltar':
            if janelaAtual== 2 :
                janela4.hide()
                janela2.un_hide()
            elif janelaAtual == 3:
                janela4.hide()
                janela3.un_hide()
        elif window == janela1 and event == 'Ganhar Poder':
            poderAtual = pa.pegaPoder()
            janela3 = telaPoder(poderAtual)
            janela1.hide()
        elif window == janela3 and event == 'Voltar':
            janela3.hide()
            janela1.un_hide()
        elif window == janela3 and event == 'Comentar':
            janela3.hide()
            janelaAtual = 3
            janela4 = telaComment(poderAtual)
        elif window == janela1 and event == 'Adicionar novo Poder':
            janela1.hide()
            janela5 = telaAddPoder()
        elif window == janela5 and event == 'Voltar':
            janela5.hide()
            janela1.un_hide()
        elif window == janela5 and event == 'Adicionar':
            if values["nomePoder"] != "" and values["desc"] != "":
                pa.addItem({"nome":values["nomePoder"],"desc":values["desc"]},pa.file1)
                janela6 = telaPoderAdicionado()
        elif window == janela6 and event == 'Voltar':
            janela6.hide()
menu()

    
