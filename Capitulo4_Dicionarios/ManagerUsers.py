from Funcoes.Funcoes import *

usuarios = {}
opcao = perguntar()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)

    if opcao == "P":
        pesquisar(usuarios, input("Qual usuário deseja procurar? ").upper())

    if opcao == "E":
        excluir(usuarios, input("Qual usuário deseja apagar? ").upper())

    if opcao == "L":
        listar(usuarios)
    opcao = perguntar()












