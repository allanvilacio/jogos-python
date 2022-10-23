import random
import utilitarios as func

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
