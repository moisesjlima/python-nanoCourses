tab = int(input("Digite um número para exibir a tabuada: "))
print("----------------------")
print("Tabuada do número ", tab)
for valor in range(1,11,1):
    print(str(tab) + " x " + str(valor) + " = " + str(tab*valor))
print("----------------------")