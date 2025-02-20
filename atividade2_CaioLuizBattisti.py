#peça ao usuario para inserir um numero. continue perguntado ate que ele insira 5 numeros e em seguida exiba a mensagem
#"o ultimo numero que voce digitou foi:" o ultimo numero que o usuario digitar
numeros = []
while len(numeros) < 5:
    num =int(input("Digite um numero: "))
    numeros.append(num)
print("O ultimo numero que voce digitou foi: ",(numeros[-1]))