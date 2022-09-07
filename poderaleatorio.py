#poder aleatório
import ast
from pyclbr import readmodule
import random
file1 = "./poder.txt"
file2 = "./comment.txt"

def addItem(item,path):
    file = open(path,"a")
    file.write(str(item)+"\n")
    file.close()
    print("adicionado :" + str(item))

def buscaItem(lista,chave,item):
    resultado = list()
    for i in lista:
        if i[chave] == item:
            resultado.append(i)
    return resultado

def loadTable(path):
    linha = dict()
    tabela = list()
    file = open(path,"r")
    for l in file.readlines():
        linha = ast.literal_eval(l)
        tabela.append(linha.copy())
    file.close()
    #print("tabela do arquivo '" + str(path)+"' carregada")
    return tabela

def listaNomePoder():
    tabela = loadTable(file1)
    lista = list()
    for linha in tabela:
        lista.append(linha["nome"])
    return lista

def addPoder():
    nome = input("digite o nome do poder:")
    desc = input("digite a descrição desse poder:")
    addItem({"nome":nome,"desc":desc},file1)

def listaPoder():
    tabela = loadTable(file1)
    print("\n --- Poderes --- \n")
    for linha in tabela:
        print("Poder: " + str(linha["nome"]) + " Descrição: " + str(linha["desc"]))

def pegaPoder():
    lista = loadTable(file1)
    poder = random.choice(lista)
    return poder


#addPoder()
#print(loadTable(file1))
#listaPoder()
#print(buscaItem(loadTable(file1),"nome","encheCaneta"))
#pegaPoder()
