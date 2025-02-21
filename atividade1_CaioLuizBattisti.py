#faça um programa que leia os numeros digitados pelo usuario, a cada numero digitado ele deve ser somado ao 
#anterior e a cada soma exibida na tela. quando a soma for superior
#a 50 ele deve exibir a mensagem "o total e:" e exibir o total e parar o programa.
total = 0
while total < 50:
    numero =int(input("Digite um numero:"))
    total += numero
    print("Soma atual: ",total)
print("o total é: ",total)
print("CAIOLUIZBATTISTI")