#Menu feito na biblioteca Tkinter
import poderaleatorio as pa #Manipulação do arquvio de poderes
import comment as cm    #Manipulação do arquivo de comentários
from tkinter import *
from ttkthemes import ThemedTk

def fecharJanela(janela):
    menu.deiconify()
    janela.destroy()

#Lista de Poderes
def listaPoderesTkinter(): 
    #funções
    def selectItem():
        print(listboxPoderes.get(ANCHOR))
    
    def fechar():
        fecharJanela(listaPoderes)

    #Instanciar Tela
    listaPoderes = Toplevel()
    #Título
    titulo = Label (listaPoderes,text="Lista de poderes").grid(column=1,row=0,padx=5,pady=5)
    #lista
    listboxPoderes = Listbox(listaPoderes,listvariable=StringVar(value=pa.listaNomePoder()))
    listboxPoderes.grid(column=1,row=1,padx=5,pady=5)
    #Botões
    comentar = Button(listaPoderes,text="Comentar", command=selectItem).grid(column=1,row=3,padx=5)
    sair = Button(listaPoderes,text="Voltar", command=fechar).grid(column=2,row=3,pady=5)
    
    #listaPoderes.mainloop()

def telaGanharPoder():
    #Funções
    def fechar():
        fecharJanela(ganharPoder)
    #Intanciar tela
    ganharPoder = Toplevel()
    ganharPoder.title("Você ganhou um poder")
    ganharPoder.minsize(250,100)
    menu.withdraw()
    texto = Text(ganharPoder,height=10,width=20)
    texto.grid(column=0,row=1,pady=5)
    texto.insert(INSERT,str(pa.pegaPoder()['desc']).encode('utf-8'))
    sair = Button(ganharPoder,text="Voltar", command=fechar).grid(column=2,row=1,pady=5)

#Menu Principal
def MenuTkinter():
    global menu
    #Instanciar menu
    menu = ThemedTk(theme="equilux")
    menu.title("Poderes Bobos")
    menu.minsize(250,100)
    #Título
    titulo = Label(menu,text= 'Poderes bobos!!!').grid(column=1,row=0,pady=5)
    #Botões
    listarPoderes = Button(menu,text="Listar Poderes",command=listaPoderesTkinter).grid(column=0,row=1,padx=5,pady=5)
    ganharPoder = Button(menu,text="Ganhar Poder", command=telaGanharPoder).grid(column=0,row=2,padx=5,pady=5)
    adicionarPoder = Button(menu,text="Adicionar Poder").grid(column=0,row=3,padx=10,pady=5)
    sair = Button(menu,text="Sair", command=menu.destroy).grid(column=0,row=4,pady=5)
    #Manter janela Aberta
    menu.mainloop()


#Inicia a interface gráfica (equivalente ao main)
MenuTkinter()
#listaPoderesTkinter()