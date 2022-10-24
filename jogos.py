import random
import utilitarios as func


def adivinhacao():
    numero_secreto = random.randint(0,10)
    print('Foi sorteado um valor entre [0-10] descubra o valor.')
    numero_jogador = func.numero_jogador()

    while numero_jogador != numero_secreto:
        continua = ' '
        while continua not in 'SN':
            continua = str(input('Valor invalido! Deseja continuar? [S/N]: ')).upper().strip()
        if continua =='N': 
            break
        numero_jogador = func.numero_jogador()
    if numero_jogador == numero_secreto:
        print('Voce descobriu o numero!')
    else:
        print('Voce desistiu!!')

    print('Numero secreto é',numero_secreto)
    print('Fim de jogo')

def forca():
    print("**************************************")
    print("**********","- Jogo da forca -" ,"*********")
    print("**************************************")

    palavra_secreta = func.selecionar_palavra_aleatoria(file='frutas.txt')
    palavra_dica = ['_' for i in range(len(palavra_secreta))]
    chances = 3

    print(palavra_secreta)

    while True:

        print(palavra_dica)
        print()
        chute = input('digite uma leta: ').upper()

        if chute in palavra_secreta:
            for index, letra in enumerate(palavra_secreta):
                if chute == letra:
                    palavra_dica[index] = chute
        else:
            chances-=1
            print('Letra não encontrada.')
            if chances > 1:
                print(f'Voce tem mais {chances} chances.')
            elif chances == 1:
                print(f'Voce tem mais {chances} chance.')
            else:
                print('Voce foi enforcado!')
                break
            if not func.deseja_continuar():
                print('Saindo do jogo!!')
                break

        print('Parabens!!')
        if palavra_dica.count('_') > 1:
            print(f'Faltam {palavra_dica.count("_")} letras')
        elif palavra_dica.count('_') == 1:
            print(f'Falta {palavra_dica.count("_")} letra')
        else:
            print('Voce ganhou!!')
            break
    print()
    print('Fim de jogo.')
