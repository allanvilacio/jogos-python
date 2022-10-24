import jogos as jg

print()
print('Selecione o jogo!!!\n\n0 - jogo da adivinhacao\n1 - jogo da forca\n')
jogo = int(input('Digite o valor: '))
print()

if jogo == 0:
    jg.adivinhacao()
elif jogo == 1:
    jg.forca()
