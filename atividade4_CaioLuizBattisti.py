#Faça um programa que peça o nome do convidado que o usuario deseja convidar para uma festa.
#Depois disso, exiba a mensagem "[nome] foi adicionado(a) com sucesso no convite!" e adicione 1 à contagem.
convidados = []
while True:
    nome =input("Digite o nome do convidado: ")
    convidados.append(nome)
    print(f"{nome} foi adicionado(a) com sucesso no convite!")
    continuar =input("voce deseja convidar outra pessoa? (s/n): ").strip().lower()
    if continuar != "s":
        print("O total de convidados é:",convidados)
        print("CAIOLUIZBATTISTI")
        break