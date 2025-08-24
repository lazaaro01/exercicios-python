import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)
    tentativas = 0

    print("Tente adivinhar o número de 1 a 10!")
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
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break
        elif chute < numero_secreto:
            print("Muito baixo. Tente novamente.")
        else:
            print("Muito alto. Tente novamente.")


jogo_adivinhacao()
