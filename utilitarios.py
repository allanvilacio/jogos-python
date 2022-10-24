
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
    
def deseja_continuar(msg='Valor invalido! Deseja continuar? [S/N]: '):
    """
    Se deseja continuar return True. Se não deseja continuar return False.
    """
    continua = ' '
    while continua not in 'SN':
        continua = str(input(msg)).upper().strip()
        if continua =='N': 
            return False
        elif continua =='S':
            return True
