import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100) 
    tentativas = 0
    menor_palpite = None
    maior_palpite = None

    print("Tente adivinhar o número de 1 a 100!")
    print("Digite 'sair' para encerrar o jogo.")

    while True:
        chute = input("Digite seu palpite: ")

        if chute.lower() == "sair":
            print("Jogo encerrado. Até a próxima!")
            break

        if not chute.isdigit():
            print("Digite um número válido ou 'sair' para sair.")
            continue

        chute = int(chute)
        tentativas += 1

        if chute == numero_secreto:
            print(f" Parabéns! Você acertou em {tentativas} tentativas.")
            break
        elif chute < numero_secreto:
            print("Muito baixo. Tente novamente.")
            if menor_palpite is None or chute > menor_palpite:
                menor_palpite = chute
        else:
            print("Muito alto. Tente novamente.")
            if maior_palpite is None or chute < maior_palpite:
                maior_palpite = chute

        if menor_palpite is not None and maior_palpite is not None:
            if menor_palpite < numero_secreto < maior_palpite:
                print(f" Dica: o número está entre {menor_palpite} e {maior_palpite}.")

jogo_adivinhacao()
