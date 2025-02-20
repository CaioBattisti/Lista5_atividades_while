#
soma = 0
while True:
    num=int(input("digite um numero: "))
    soma += num
    continuar =input("Deseja adicionar ultro numero? (s/n)").strip().lower()
    if continuar != 's':
        break
    print("")