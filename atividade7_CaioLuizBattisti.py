#Escreva um programa que permaneça em laço lendo números inteiros. 
#O laço termina quando for digitado 0 (zero).
#Cada valor diferente de zero digitado deve ser colocado em uma lista, desde que ele ainda não esteja lá,
#ou seja valores repetidos não são aceitos. 
#Se um valor repetido for digitado, o programa deve exibir uma mensagem na tela. 
#Ao final exiba a lista e a quantidade de elementos que ela contém.
numeros = []
while True:
    num =int(input("Digite um numero: "))
    if num not in numeros:
        numeros.append(num)
    elif num == 0:
        print("O total dos numero sao: ",numeros)
        print("CAIOLUIZBATTISTI")
        break

    