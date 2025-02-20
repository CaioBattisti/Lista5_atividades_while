#faça um programa que leia os numeros digitados pelo usuario, a cada numero digitado ele deve ser somado ao 
#anterior e a cada soma exibida na tela. quando a soma for superior
#a 50 ele deve exibir a mensagem "o total e:" e exibir o total e parar o programa.
numeros = 0
while True:
    num1 =int(input("Digite um numero"))
    numeros += num1
    if numeros > 50:
        print("O total é:",numeros)
    break
else:
    print("Soma parcial:",numeros)