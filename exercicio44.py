import time

def start_game():
    print("Bem-vindo ao 'O Mistério da Fama Perdida'!")
    print("As celebridades desapareceram! Só tu as podes salvar.")
    time.sleep(2)

    score= 0

    # Desafio 1- Óscares
    print("Desafio 1: Óscares")
    print("Qual destes filmes ganhou Óscar de Melhor filme em 2024?")
    print("a) Oppenheimer\nb) Barbie\nc) Anatomia de uma Queda\nd) Poor Things")
    answer = input("Resposta: ") .lower()

    if answer == "a" or answer == "oppenheimer":
        print("Correto!")
        score += 1
    else:
        print("Errado! Era 'oppenheimer'.")
    time.sleep(1)

    # Desafio 2- Letras Misturadas
    print("\nDesafio 2: Letras Misturadas")
    print("Quem é esta cantora famosa? 'LORATY SWIFT' ")
    answer = input("Resposta: "). lower()

    if "taylor swift" in answer:
        print("Correto! ")
        score += 1
    else:
        print("Errado! Era 'Taylor Swift'.")
    time.sleep(1)

    # Desafio 3
    print("\n3. Zendaya já ganhou um Emmy? (V/F)")
    a = input("Resposta: ").strip().lower()
    if a.startswith("v"):
        print("Correto!")
        score += 1
    else:
        print("Errado. Ela já ganhou.")
    time.sleep(1)

    # Desafio 4
    print("\n4. Quem canta 'I can buy myself flowers'?")
    a = input("Resposta: ").strip().lower()
    if "miley" in a and "flowers" in a:
        print("Correto!")
        score += 1
    else:
        print("Errado. Era Miley Cyrus - Flowers.")
    time.sleep(1)

    # Resultado
    print("\nPontuação final:", score, "/ 4")
    if score == 4:
        print("Exclente!")
    elif score >= 3:
        print("Perfeito!")
    elif score >= 2:
        print("Nada mal! Mas dá para melhorar.")
    elif score >= 1:
        print("Faz outra vez!")
    else:
        print("Ups! Tenta outra vez.")
    time.sleep(1)
    print("Obrigado por jogar!")

start_game()


