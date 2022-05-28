"""
#Lista preenchida estaticamente
lista_estatica = ["xpto", True]
#Dinamicamente
lista_dinamica = [input("Digite o usuário: "), bool(int(input("Está logado? ")))]
#vazia
lista_vazia = []
"""
inventario = []
resposta = 'S'
while resposta == 'S':
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("N° Serial: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Digite 'S' para continuar: ").upper()

for elemento in inventario:
    print("\t",elemento)


