#Crie uma variável chamada “adivinha” e defina o valor como 50.Peça ao usuário para inserir um número.
#Embora o palpite não seja o mesmo que o valor do “adivinha”,diga a ele se o palpite é muito baixo ou muito alto epeça que ele dê outro palpite.
#Se ele inserir o mesmo valor que “adivinha”, exiba a mensagem "Parabéns! Você acertou o número em {} tentativas!"
adivinha = 50
tentativas = 0
while True:
    tentativa=int(input("Digite um numero: "))
    tentativas += 1
    if tentativa < adivinha:
        print("Palpite muito baixo! Tente novamente.")
    elif tentativa > adivinha:
        print("palpite muito alto! Tente novamente")
    else:
        print("Parabens! Voce acertou o numero em",tentativas,"tentativas!")
        break