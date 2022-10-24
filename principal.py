import jogos as jg



print('Selecione o jogo!!!\n\n0 - jogo da adivinhacao\n1 - jogo da forca\n\n')
jogo = int(input('Digite o valor: '))

if jogo == 0:
    jg.adivinhacao()
elif jogo == 1:
    jg.forca()
