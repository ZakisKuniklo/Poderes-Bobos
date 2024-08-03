#Menu feito na biblioteca Tkinter
import poderaleatorio as pa
import comment as cm
from tkinter import *

#Menu Principal
def MenuTkinter():
    #Instanciar menu
    menu = Tk()
    menu.title("Poderes Bobos")
    menu.minsize(250,100)
    #Título
    titulo = Label(menu,text= 'Poderes bobos!!!').grid(column=1,row=0)
    #Botões
    listarPoderes = Button(menu,text="Listar Poderes").grid(column=0,row=1)
    ganharPoder = Button(menu,text="Ganhar Poder").grid(column=0,row=2,padx=10, pady=10)

    #Manter janela Aberta
    menu.mainloop()




#Inicia a interface gráfica (equivalente ao main)
MenuTkinter()