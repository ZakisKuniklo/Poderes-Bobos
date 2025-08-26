#Menu feito na biblioteca Tkinter
import poderaleatorio as pa #Manipulação do arquvio de poderes
import comment as cm    #Manipulação do arquivo de comentários
from tkinter import *
from ttkthemes import ThemedTk

def fecharJanela(anterior,janela):
    anterior.deiconify()
    janela.destroy()

#Lista de Poderes
def listaPoderesTkinter(): 
    #funções
    def selectItem():
        print(listboxPoderes.get(ANCHOR))
        telaListarComentario("comentario")
     
    def fechar():
        fecharJanela(menu,listaPoderes)
    
    #Instanciar Tela
    global listaPoderes
    listaPoderes = Toplevel()
    menu.withdraw()
    #Título
    titulo = Label (listaPoderes,text="Lista de poderes").grid(column=1,row=0,padx=5,pady=5)
    #lista
    listboxPoderes = Listbox(listaPoderes,listvariable=StringVar(value=pa.listaNomePoder()))
    listboxPoderes.grid(column=1,row=1,padx=5,pady=5)
    #Botões
    comentar = Button(listaPoderes,text="Comentar", command=selectItem).grid(column=1,row=3,padx=5)
    sair = Button(listaPoderes,text="Voltar", command=fechar).grid(column=2,row=3,pady=5)
    #listaPoderes.mainloop()

def telaListarComentario(comentario):
    def fechar():
        fecharJanela(listaPoderes,telaListarComentario)
    #Instanciar Tela
    telaListarComentario = Toplevel()
    telaListarComentario.minsize(250,100)
    listaPoderes.withdraw()
    #Botões
    sair = Button(telaListarComentario,text="Voltar", command=fechar).grid(column=2,row=3,pady=5)

def telaGanharPoder():
    #Funções
    def fechar():
        fecharJanela(menu,ganharPoder)
    #Intanciar tela
    ganharPoder = Toplevel()
    ganharPoder.title("Você ganhou um poder")
    ganharPoder.minsize(250,100)
    #ganharPoder.overrideredirect(True)
    menu.withdraw()
    poder = pa.pegaPoder()
    print(poder)
    titulo = Label(ganharPoder,text=str(poder['nome']).encode('utf-8'))
    titulo.grid(column=0,row=0,pady=5)
    texto = Text(ganharPoder,height=10,width=20)
    texto.grid(column=0,row=1,pady=5)
    texto.insert(INSERT,str(poder['desc']).encode('utf-8'))
    sair = Button(ganharPoder,text="Voltar", command=fechar).grid(column=2,row=1,pady=5)


def telaAdicionarPoder():
    #Funções
    def fechar():
        fecharJanela(menu,adicionarPoder)
    def armazenarPoder():
        nomePoder = entryNome.get()
        print(nomePoder)
        descricaoPoder = textDescricao.get("1.0",END)
        print(descricaoPoder)
    #Instanciar janela
    adicionarPoder = Toplevel()
    adicionarPoder.title("Adicionar Novo Poder")
    adicionarPoder.minsize(250,100)
    menu.withdraw()
    titulo = Label(adicionarPoder,text= 'Adicionar Novo Poder').grid(column=1,row=0,pady=5)
    labelNome = Label(adicionarPoder,text= 'Nome:').grid(column=0,row=1,pady=5)
    entryNome = Entry(adicionarPoder)
    entryNome.grid(column=1,row=1,pady=5)
    lableDescricao = Label(adicionarPoder,text= 'Descricao:').grid(column=0,row=2,pady=5)
    textDescricao = Text(adicionarPoder,height=10,width=20)
    textDescricao.grid(column=1,row=2,pady=5)
    botaoAdicionarPoder = Button(adicionarPoder,text="Adicionar poder", command=armazenarPoder).grid(column=1,row=3,pady=5)
    sair = Button(adicionarPoder,text="Voltar", command=fechar).grid(column=1,row=4,pady=5)

#Menu Principal
def MenuTkinter():
    global menu
    #Instanciar menu
    menu = ThemedTk(theme="equilux")
    menu.title("Poderes Bobos")
    menu.minsize(250,100)
    menu.resizable(0,0)
    #Título
    titulo = Label(menu,text= 'Poderes bobos!!!').grid(column=1,row=0,pady=5)
    #Botões
    listarPoderes = Button(menu,text="Listar Poderes",command=listaPoderesTkinter).grid(column=1,row=1,padx=5,pady=5)
    ganharPoder = Button(menu,text="Ganhar Poder", command=telaGanharPoder).grid(column=1,row=2,padx=5,pady=5)
    adicionarPoder = Button(menu,text="Adicionar Poder",command=telaAdicionarPoder).grid(column=1,row=3,padx=10,pady=5)
    sair = Button(menu,text="Sair", command=menu.destroy).grid(column=1,row=4,pady=5)
    #Manter janela Aberta
    menu.mainloop()


#Inicia a interface gráfica (equivalente ao main)
MenuTkinter()
#listaPoderesTkinter()
