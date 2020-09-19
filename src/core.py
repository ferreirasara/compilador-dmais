def analex():
    pass

def prox_char():
    pass

def grava_token(token, lexema):
    pass

if __name__ == '__main__':
    ch = prox_char()
    while True:
        (token, lexema) = analex()
        grava_token(token, lexema)