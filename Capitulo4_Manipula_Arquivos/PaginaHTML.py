with open ("pagina.html", "w") as pagina:
    pagina.write("<body>\n<h1> Este é um teste pagina Web </h1>")
    pagina.write("\n<h1> Nomes <strong>Importantes</strong> para o projeto </h1>")
    pagina.write("\n<h4>")
    nome=""
    username = ""
    while nome !="SAIR":
        nome= input("Digite um nome ou SAIR: ").upper()
        username = nome.capitalize()
        if nome!="SAIR":
            pagina.write("Bem vindo "+username+" <br>")

    pagina.write("</h4>\n</body>")