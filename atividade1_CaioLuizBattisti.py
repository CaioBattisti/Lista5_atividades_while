#faça um programa que leia os numeros digitados pelo usuario, a cada numero digitado ele deve ser somado ao 
#anterior e a cada soma exibida na tela. quando a soma for superior
#a 50 ele deve exibir a mensagem "o total e:" e exibir o total e parar o programa.
num1 =int(input("Digite um numero: "))
num2 =int(input("Digite um numero: "))
numeros = num1 + num2
while numeros < 50:
    print("O total é: {}".format(numeros))