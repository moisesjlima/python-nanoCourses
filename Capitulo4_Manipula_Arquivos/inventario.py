from Funcoes.Funcoes_files import *
inventario = {}
opcao=chamarMenu()
while opcao>0 and opcao<4:
    if opcao == 1:
        registrar(inventario)

    elif opcao == 2:
        persistir(inventario)

    elif opcao == 3:
        resultado = exibir()
        for linha in resultado:
            print(linha[linha.find(";")+1:-1])
            #print(linha[2:-1])
    opcao = chamarMenu()

"""
# find() -> Método que retorna o a string apartir da letra especificada ex linha.find(";")+1:-1
# #Irá encontrar a 1° string ";" e escrever o que está após ela(+1)
for linha in resultado:
        separacao=linha[linha.find(";")+1:-1]
        data=separacao[0:separacao.find(";")]
        separacao = separacao[separacao.find(";")+1:-1]
        descricao=separacao[0:separacao.find(";")]
        departamento=linha[linha.rfind(";")+1:-1]
        print("\nData.........: ", data)
        print("Descrição....: ", descricao)
        print("Departamento.: ", departamento)
#opcao = chamarMenu() """

#split -> função que quebra a string de acordo com o delimitador especificado, e separa essas informações
#em listas com as posições
for linha in resultado:
    lista=linha.split(";")
    print("Data.........: ", lista[1])
    print("Descrição....: ", lista[2])
    print("Departamento.: ", lista[3])

