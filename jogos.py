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

    palavra_secreta = 'banana'
    palavra_dica = ['_' for i in range(len(palavra_secreta))]

    print(palavra_secreta)

    while (palavra_dica.count('_') > 0):
        print(palavra_dica)
        print(f'Faltam {palavra_dica.count("_")} letras')
        chance = input('digite uma leta: ')
        for index, letra in enumerate(palavra_secreta):
            if chance == letra:
                palavra_dica[index] = chance
        if chance not in palavra_secreta: 
            print('Letra não encontrada.')
            if not func.deseja_continuar():
                print('Saindo do jogo!!')
                break
        
forca()