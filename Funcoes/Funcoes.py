def perguntar():
 resposta = input("O que deseja realizar? "

 +      "\n<I> - Para inserir um usuário"

 +      "\n<P> - Para pesquisar um usuário"

 +      "\n<E> - Para Excluir um usuário"

 +      "\n<L> - Para listar um usuário: ").upper()
 return resposta

def inserir(dicionario):
 chave = input("Digite o login: ").upper()
 """nome = input("Digite o nome: ").upper()
 data = input("Digite a última data de acesso: ")
 estacao = input("Qual a última estação acessada: ").upper()
 usuarios[chave]=[nome, data, estacao]"""
 dicionario[chave] = [input("Digite o nome: ").upper(),
                    input("Digite a última data de acesso: "),
                    input("Qual a última estação acessada: ").upper()]

def pesquisar(dicionario, chave):
 list = dicionario.get(chave)
 if list != None:
  print("\nNome............: " + list[0])
  print("\nÚltimo acesso...: " + list[1])
  print("\nÚltima estação..: " + list[2])
def excluir(dicionario, chave):
 if dicionario.get(chave) != None:
  del dicionario[chave]
 print("Objeto ", chave  ," Eliminado!")

def listar(dicionario):
 for chave, valor in dicionario.items():
  print("Objeto........")
  print("Login.: ", chave)
  print("Dados.:", valor)

