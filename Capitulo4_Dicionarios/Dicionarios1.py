usuarios = {} #Representação de um dicionário "{}"
usuarios = {
    "Chaves": ["chaves silva", "17/06/2017", "Recep_01"],
    "Quico": ["Quico Flores", "03/06/2017", "Raiox_02"],
    "Florinda": ["Florinda Flores", "13/06/2017", "Recep_1"]
}

#print(usuarios["Florinda"])
usuarios["Madruga"] = ["Seu madruga", "01/12/2016"]
print(usuarios)
print(" ")
print("Dados Chaves ", usuarios["Chaves"])
print(" ")
print("Dados Chaves ", usuarios.get("Chaves"))
print("Dados Quico ", usuarios.get("Quico"))
print("Dados Florinda ", usuarios.get("Florinda"))
print("Dados madruga ", usuarios.get("Madruga"))
##print(usuarios.clear())

print(usuarios)