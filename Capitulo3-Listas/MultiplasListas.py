equipamentos = []
valores = []
seriais = []
departamento = []
resposta = 'S'
while resposta == 'S':
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("N° Serial: ")))
    departamento.append(input("Departamento: "))
    resposta = input("Digite 'S' para continuar: ").upper()
    for indice in range(0,len(equipamentos)):
        print("equipamentos..:", (indice+1))
        print("Nome.....: ", equipamentos[indice])
        print("valores.....: ", valores[indice])
        print("Serial.....: ", seriais[indice])
        print("Departamento.....: ", departamento[indice])

busca = input("Buscar equipamento: ")
for indice in range(0,len(equipamentos)):
    if busca == equipamentos[indice]:
        print("Equipamento..: ", equipamentos[indice])
        print("Valor..: ", valores[indice])
        print("Serial..: ", seriais[indice])


"""
for equipamento in equipamentos:
    print(equipamento)
for valor in valores:
    print(valor)
    
#print("equipamento1: ", equipamento[0], " valor: " , valores[0], " com n° serial: ", seriais[0])"""