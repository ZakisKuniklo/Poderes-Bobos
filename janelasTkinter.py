#Menu feito na biblioteca Tkinter
import poderaleatorio as pa #Manipulação do arquvio de poderes
import comment as cm    #Manipulação do arquivo de comentários
from tkinter import *


#Lista de Poderes
def listaPoderesTkinter():
    #Instanciar Tela
    listaPoderes = Toplevel()
    listaPoderes.title("Lista de poderes")
    listaPoderes.minsize(250,100)
    #Título
    titulo = Label (listaPoderes,text="Lista de poderes").grid(column=1,row=0,padx=5,pady=5)
    #lista
    listboxPoderes = Listbox(listaPoderes,listvariable=StringVar(value=pa.listaNomePoder()))
    listboxPoderes.grid(column=1,row=1,padx=5,pady=5)
    #Botões
    comentar = Button(listaPoderes,text="Comentar").grid(column=1,row=3,padx=5)
    sair = Button(listaPoderes,text="Voltar", command=listaPoderes.destroy).grid(column=2,row=3,pady=5)
    
    
    #listaPoderes.mainloop()


#Menu Principal
def MenuTkinter():
    #Instanciar menu
    menu = Tk()
    menu.title("Poderes Bobos")
    menu.minsize(250,100)
    #Título
    titulo = Label(menu,text= 'Poderes bobos!!!').grid(column=1,row=0,pady=5)
    #Botões
    listarPoderes = Button(menu,text="Listar Poderes",command=listaPoderesTkinter).grid(column=0,row=1,padx=5,pady=5)
    ganharPoder = Button(menu,text="Ganhar Poder").grid(column=0,row=2,padx=5,pady=5)
    adicionarPoder = Button(menu,text="Adicionar Poder").grid(column=0,row=3,padx=10,pady=5)
    sair = Button(menu,text="Sair", command=menu.destroy).grid(column=0,row=4,pady=5)
    #Manter janela Aberta
    menu.mainloop()


#Inicia a interface gráfica (equivalente ao main)
MenuTkinter()
#listaPoderesTkinter()