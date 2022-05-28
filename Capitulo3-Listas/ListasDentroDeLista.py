inventario =[]
resposta = 'S'
while resposta == 'S':
    equipamento = [
        input("Equipamento: "),
        float(input("Valor: ")),
        int(input("Número Serial: ")),
        input("Departamento: ")
    ]
    inventario.append(equipamento)
    resposta = input("Digite \"S\" para continuar..: ").upper()

for elemento in inventario:
    print("---------------------")
    print("Nome...........: ", elemento[0])
    print("Valor..........: ", elemento[1])
    print("Serial.........: ", elemento[2])
    print("Departamento...: ", elemento[3])

valores = []
for elemento in inventario:
    valores.append(elemento[1])
if len(valores)>0:
    print("O equipamento mais caro custa -> ", max(valores))
    print("O equipamento mais barato custa -> ", min(valores))

print("Valor total de equipamentos é -> ", sum(valores))

