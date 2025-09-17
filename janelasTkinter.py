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
        #print(listboxPoderes.get(ANCHOR))
        telaListarComentario(listboxPoderes.get(ANCHOR))
     
    def fechar():
        fecharJanela(menu,listaPoderes)
    
    #Instanciar Tela
    global listaPoderes
    listaPoderes = Toplevel()
    listaPoderes.minsize(250,100)
    menu.withdraw()
    #Título
    titulo = Label (listaPoderes,text="Lista de poderes").grid(column=1,row=0,padx=5,pady=5)
    #lista
    listboxPoderes = Listbox(listaPoderes,listvariable=StringVar(value=pa.listaNomePoder()))
    listboxPoderes.grid(column=1,row=1,padx=5,pady=5)
    #Botões
    comentar = Button(listaPoderes,text="Comentários", command=selectItem).grid(column=1,row=3,padx=5)
    sair = Button(listaPoderes,text="Voltar", command=fechar).grid(column=1,row=4,pady=5)
    #Espaçadores
    um = Label(listaPoderes,text= ' ').grid(column=0,row=0,padx=25)
    dois = Label(listaPoderes,text= ' ').grid(column=0,row=1,padx=25)
    tres = Label(listaPoderes,text= ' ').grid(column=0,row=2,padx=25)
    quatro = Label(listaPoderes,text= ' ').grid(column=0,row=3,padx=25)
    #listaPoderes.mainloop()

def telaListarComentario(poder):
    #Instanciar Lisa de Comentários
    comentarios = cm.showComment(poder)
    print(comentarios)
    lista = list()
    for i in comentarios:
        lista.append("usuário: "+ str(i["nome"]) + " poder: "+ str(i["poder"])+ "\n"+ str(i["data"]) + "\n"+str(i["comment"]))
    bigString = ""
    for t in lista:
        bigString = bigString + t + "\n"
    #Funções 
    def fechar():
        fecharJanela(listaPoderes,listarComentario)
    def acessarComentario():
        telaAdicionarComentario(poder)
    #Instanciar Tela
    listarComentario = Toplevel()
    listarComentario.minsize(250,220)
    listaPoderes.withdraw()
    #lista
    #listboxPoderes = Listbox(telaListarComentario,listvariable=StringVar(value=lista))
    #listboxPoderes.grid(column=1,row=1,padx=15,pady=5)
    bigLista =  Text(listarComentario,yscrollcommand = True, xscrollcommand=True)
    bigLista.grid(column=1,row=0,padx=5,pady=5)
    bigLista.insert(END,bigString)
    #Botões
    comentar = Button(listarComentario,text="Comentar", command=acessarComentario).grid(column=1,row=3,pady=5)
    sair = Button(listarComentario,text="Voltar", command=fechar).grid(column=1,row=4,pady=5)

def telaAdicionarComentario(poder):
    #Funções
    def fechar():
        fecharJanela(menu,adicionarComentario)
    def addCommentario():
        nick = entryNick.get()
        comment = textComment.get("1.0",END).rstrip()
        if (nick != "" and comment!= ""):
            cm.addComment(nick,poder,comment)
        textComment.delete("1.0",END)
        entryNick.delete(0,END)
    #Instanciar tela
    adicionarComentario = Toplevel()
    adicionarComentario.title("Adicionar Novo Comentário")
    adicionarComentario.minsize(250,100)
    #Campos
    titulo = Label(adicionarComentario,text= 'Adicionar Novo Comentário').grid(column=1,row=0,pady=5)
    nomePoder = Label(adicionarComentario,text= poder).grid(column=1,row=1,pady=5)
    entryLabel= Label(adicionarComentario,text= 'Usuário:').grid(column=0,row=2,pady=5)
    entryNick = Entry(adicionarComentario)
    entryNick.grid(column=1,row=2,pady=5)
    textLabel= Label(adicionarComentario,text= 'Comentário:').grid(column=0,row=3,pady=5)
    textComment = Text(adicionarComentario,height=10,width=20)
    textComment.grid(column=1,row=3,pady=5)
    #Botões
    comentar = Button(adicionarComentario,text="Comentar", command=addCommentario).grid(column=1,row=4,pady=5)
    sair = Button(adicionarComentario,text="Voltar", command=fechar).grid(column=1,row=5,pady=5)

def telaGanharPoder():
    #Funções
    def fechar():
        fecharJanela(menu,ganharPoder)
    #Intanciar tela
    ganharPoder = Toplevel()
    ganharPoder.title("Você ganhou um poder")
    ganharPoder.minsize(250,100)
    ganharPoder.resizable(0,0)
    #ganharPoder.overrideredirect(True)
    menu.withdraw()
    poder = pa.pegaPoder()
    print(poder)
    titulo = Label(ganharPoder,text=str(poder['nome']).encode('utf-8'))
    titulo.grid(column=1,row=0,pady=5)
    texto = Text(ganharPoder,height=10,width=20)
    texto.grid(column=1,row=1,pady=5)
    texto.insert(INSERT,str(poder['desc']).encode('utf-8'))
    sair = Button(ganharPoder,text="Voltar", command=fechar).grid(column=1,row=2,pady=5)
    #Espaçadores
    um = Label(ganharPoder,text= ' ').grid(column=0,row=0,padx=15)
    dois = Label(ganharPoder,text= ' ').grid(column=0,row=1,padx=15)
    tres = Label(ganharPoder,text= ' ').grid(column=0,row=2,padx=15)

def telaAdicionarPoder():
    #Funções
    def fechar():
        fecharJanela(menu,adicionarPoder)
    def armazenarPoder():
        nomePoder = entryNome.get()
        descricaoPoder = textDescricao.get("1.0",END)
        descricaoPoder = descricaoPoder.rstrip()
        pa.addItem({"nome":nomePoder,"desc":descricaoPoder},pa.file1)
        textDescricao.delete("1.0",END)
        entryNome.delete(0,END)
        telaPoderAdicionado(adicionarPoder)
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

def telaPoderAdicionado(telaPoder):
    #Funções
    def fechar():
        fecharJanela(telaPoder,poderAdicionado)
    #Instanciar janela
    poderAdicionado = Toplevel()
    poderAdicionado.title("Poder Adicionado")
    poderAdicionado.minsize(250,100)
    poderAdicionado.resizable(0,0)
    titulo = Label(poderAdicionado,text= 'Poder Adicionado!').grid(column=1,row=0,pady=5)
    sair = Button(poderAdicionado,text="Voltar", command=fechar).grid(column=1,row=4,pady=5)


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
    listarPoderes = Button(menu,text="Listar Poderes",command=listaPoderesTkinter).grid(column=1,row=1,pady=5)
    ganharPoder = Button(menu,text="Ganhar Poder", command=telaGanharPoder).grid(column=1,row=2,pady=5)
    adicionarPoder = Button(menu,text="Adicionar Poder",command=telaAdicionarPoder).grid(column=1,row=3,pady=5)
    sair = Button(menu,text="Sair", command=menu.destroy).grid(column=1,row=4,pady=5)
    #Espaçadores
    um = Label(menu,text= ' ').grid(column=0,row=0,padx=32)
    dois = Label(menu,text= ' ').grid(column=0,row=1,padx=32)
    tres = Label(menu,text= ' ').grid(column=0,row=2,padx=32)
    quatro = Label(menu,text= ' ').grid(column=0,row=3,padx=32)
    cinco = Label(menu,text= ' ').grid(column=0,row=4,padx=32)
    #Manter janela Aberta
    menu.mainloop()


#Inicia a interface gráfica (equivalente ao main)
MenuTkinter()
#listaPoderesTkinter()
