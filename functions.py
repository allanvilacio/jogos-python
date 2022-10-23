
def numero_jogador(msg='Digite o valor: '):
    passe = True
    while passe:
        try:
            numero = int(input(msg))
        except:
            print('Valor invalido tente novamente!')
            pass
        else:
            passe =False
    return numero
    