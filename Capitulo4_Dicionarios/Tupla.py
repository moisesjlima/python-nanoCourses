#Tupla -> imutável memória volatil

"""ips = {}
resp = "S"
while resp == "S":
    ips[(input("Digite os dois primeiros octetos: "),)


for ip in ips.keys():
    print(ip[0]+"."+ip[1])

print("\nExibindo máquinas com o mesmo endereço: ")
pesquisa = input("Digite os dois últimos octetos: ")
for ip,nome in ips.items():
    print("Máquinas no mesmo endereço (redes diferentes)")
    if(ip[1]==pesquisa):
        input("Digite os dois últimos octetos: "))]= input("Nome da máquina: ")
    resp = input("Sigite \"S\" para continuar ").upper(
        print(nome)

print("\nExibindo máquinas que compõem uma mesma rede: ")
rede = input("Digite os dois primeiros octetos: ")
for ip,nome in ips.items():
    if(ip[1]==rede):
        print(nome) """
usuarios={}
resp="S"
emails=[]
while resp=="S":
    emails.append(input("Digite um email: ").lower())
    resp = input("Deseja inserir outro email? <S> para continuar: ").upper()

for email in emails:
    print(email)


tupla = list(enumerate(emails))
for chave in range(90,len(tupla)):
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]]=input("Digite o nome: "), input("Digite o nível: ")

for chave,dado in usuarios.items():
    print("Usuários.: ", chave[0])
    print("Email.: ", chave[1])
    print("Nome.: ", dado[0])
    print("Nível.: ", dado[1])
