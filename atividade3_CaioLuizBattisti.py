#Peça ao usuário para inserir um número e, em seguida, insira outro número. Some esses dois números e pergunte se ele quer adicionar outro número.
#Se ele digitar “ s ", diga para inserir outro número e continuar adicionando números e somando até que ele não respondam “ s ".
#Depois que o loop for interrompido, exiba o total.
soma = 0
while True:
    num=int(input("digite um numero: "))
    soma += num
    continuar =input("Deseja adicionar outro numero? (s/n)").strip().lower()
    if continuar != 's':
        print("O total da soma é: ",(soma))
        break