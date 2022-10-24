import random
from unidecode import unidecode

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

def selecionar_palavra_aleatoria(file= 'frutas.txt', start=0, upper=True, remove_acento=True):
    with open(file) as arquivo:
        frutas = [fruta.strip() for fruta in arquivo]
    rand = random.randrange(start, len(frutas))
    fruta = frutas[random.randrange(start,len(frutas))]
    if upper:
        fruta = fruta.upper()
    if remove_acento:
        fruta = unidecode(fruta)
    return fruta