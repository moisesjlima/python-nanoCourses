par = 0
impar = 0
for num in range(1, int(input("Número para determinar o fim da contagem: ")), 1):
    print("\t"+str(num))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1


print("Dos números digitados " + str(par) +
      " são pares\ne " + str(impar) + " são impares")
