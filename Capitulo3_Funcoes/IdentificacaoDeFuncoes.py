"""def acrescentaPorcentagem(valor, porcentagem):
    tot = (valor * porcentagem) / 100
    return tot + valor
def removePorcentagem(valor, porcentagem):
    tot = (valor * porcentagem) / 100
    if tot > valor:
        return print("Valor ficara negativo!!!")
    else:
        return valor - tot
print(acrescentaPorcentagem(100,10))
print(removePorcentagem(100,50)) """

def preencherInventario(list):
    resp = "S"
    while resp == "S":
        equipamento = [
            input("Equipamento: "),
            float(input("Valor: ")),
            int(input("Número Serial: ")),
            input("Departamento: ")
        ]
        list.append(equipamento)
        resp = input("Digite \"S\" para continuar: ").upper()

def exibirLista(list):
    for elemento in list:
        print("---------------------")
        print("Nome...........: ", elemento[0])
        print("Valor..........: ", elemento[1])
        print("Serial.........: ", elemento[2])
        print("Departamento...: ", elemento[3])

def localizaPorNome(list):
    busca = input("Nome do equipamento que deseja buscar: ")
    for elemento in list:
        if busca == elemento[0]:
            print("Buscando dados..................\n")
            print("\tNome...........: ", elemento[0])
            print("\tValor..........: ", elemento[1])
            print("\tSerial.........: ", elemento[2])
            print("\tDepartamento...: ", elemento[3])

def excluirPorSerial(list):
        serial = int(input("Digite o serial do equipamento para ser removido: "))
        for elemento in list:
            if elemento[2] == serial:
                list.remove(elemento)
                return print("\nO elemento " + elemento[0] + " foi excluído...")