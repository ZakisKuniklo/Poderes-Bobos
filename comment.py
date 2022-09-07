#comentários
import poderaleatorio
from datetime import datetime

def addComment(poder):
    comentario = dict()
    comentario["nome"] = input("insira seu nome: ")
    comentario["poder"] = poder["nome"]
    comentario["comment"] = input("insira seu comentário:")
    comentario["data"] = datetime.now().strftime('%d/%m/%Y %H:%M')
    poderaleatorio.addItem(comentario,poderaleatorio.file2)

def showComment(nomePoder):
    lista =poderaleatorio.loadTable(poderaleatorio.file2)
    comentarios = poderaleatorio.buscaItem(lista,"poder",nomePoder)
    return comentarios
    #for i in sorted(comentarios):
        #print("usuário: "+ str(i["nome"]) + " poder: "+ str(i["poder"])+ "\n"+ str(i["data"]) + "\n"+str(i["comment"]))

poder = poderaleatorio.buscaItem(poderaleatorio.loadTable(poderaleatorio.file1),"nome","encheCaneta")
#print(poder)
#addComment(poder[0])
showComment(poder[0]["nome"])