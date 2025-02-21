#Peça ao usuário para inserir um número entre 15 e 20.
#Se ele inserir um valor abaixo de 15, exiba a mensagem "Muito baixo" e peça que tentem novamente.
#Se ele inserir um valor acima de 20, exiba a mensagem "Muito alto" e peça que tentem novamente.
#Continue repetindo isso até que ele insira um valor entre 15 e 20 e, em seguida, exibam a mensagem "Obrigado".
while True:
    numero=int(input("Digite um numero entre 15 e 20: "))
    if numero < 15:
        print("numero muito baixo! Tente de novo.")
        print("CAIOLUIZBATTISTI")
    elif numero > 20:
        print("numero muito alto! Tente de novo.")
        print("CAIOLUIZBATTISTI")
    else:
        print("Obrigado")
        print("CAIOLUIZBATTISTI")
        break