import sys

contador = -1
entrada = ''

def grava_token(arquivo, token, lexema):
    if token != None and lexema != None:
        arquivo.write(str(token).ljust(20, ' '))
        arquivo.write(' | ')
        arquivo.write(str(lexema))
        arquivo.write('\n')

def volta_um():
    global contador
    contador -= 1

def prox_char():
    global entrada
    global contador
    if contador < len(entrada)-1:
        contador += 1
    return entrada[contador]

def letra(c):
    return ord(c) in range(65, 91) or ord(c) in range(97, 123)

def simbolo(c):
    return ord(c) in [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 58, 59, 60, 61, 62, 63, 91, 93, 95, 123, 124, 125]

def fim():
    global entrada
    global contador
    if contador < len(entrada)-1:
        return False
    else:
        return True

def analex():
    if fim():
        return 'FIM', None

    global entrada
    global contador
    c = prox_char()
    lexema = c
    
    if c.isdigit():
        while True: # Enquanto for um digito, incrementa o lexema
            c = prox_char()
            if c.isdigit():
                lexema += c
            else:
                break
        if c in [' ', ';', '\n']: # Se acabaram os digitos retorna um inteiro
            volta_um()
            return 'LB_INT', lexema
        elif c == '.': # Caso possua ponto, é um float
            lexema += c
            c = prox_char()
            if not(c.isdigit()): # Caso não exista um digito depois do ponto, é um erro
                return 'ERRO', None
            else:
                while True: # Enquanto for um digito, incrementa o lexema
                    c = prox_char()
                    if c.isdigit():
                        lexema += c
                    else:
                        break
                if c in [' ', ';', '\n']: # Se acabaram os digitos retorna um float
                    volta_um()
                    return 'LB_FLOAT', lexema
                else:
                    return 'ERRO', None
        else:
            return 'ERRO', None
    elif c in ['\t', '\n', ' ']:
        return None, None
    elif letra(c):
        if c == 'v':
            c = prox_char()
            if c == 'o':
                lexema += c
                c = prox_char()
                if c == 'i':
                    lexema += c
                    c = prox_char()
                    if c == 'd':
                        lexema += c
                        return 'LB_VOID', lexema
        elif c == 'i':
            c = prox_char()
            if c == 'n':
                lexema += c
                c = prox_char()
                if c == 't':
                    lexema += c
                    return 'LB_INT', lexema
            if c == 'f':
                lexema += c
                return 'LB_IF', lexema
        elif c == 'c':
            c = prox_char()
            if c == 'h':
                lexema += c
                c = prox_char()
                if c == 'a':
                    lexema += c
                    c = prox_char()
                    if c == 'r':
                        lexema += c
                        return 'LB_CHAR', lexema
            if c == 'o':
                lexema += c
                c = prox_char()
                if c == 'n':
                    lexema += c
                    c = prox_char()
                    if c == 't':
                        lexema += c
                        c = prox_char()
                        if c == 'i':
                            lexema += c
                            c = prox_char()
                            if c == 'n':
                                lexema += c
                                c = prox_char()
                                if c == 'u':
                                    lexema += c
                                    c = prox_char()
                                    if c == 'e':
                                        lexema += c
                                        return 'LB_CONTINUE', lexema
        elif c == 'b':
            c = prox_char()
            if c == 'o':
                lexema += c
                c = prox_char()
                if c == 'o':
                    lexema += c
                    c = prox_char()
                    if c == 'l':
                        lexema += c
                        return 'LB_BOOL', lexema
            if c == 'r':
                lexema += c
                c = prox_char()
                if c == 'e':
                    lexema += c
                    c = prox_char()
                    if c == 'a':
                        lexema += c
                        c = prox_char()
                        if c == 'k':
                            lexema += c
                            return 'LB_BREAK', lexema
        elif c == 't':
            c = prox_char()
            if c == 'r':
                lexema += c
                c = prox_char()
                if c == 'u':
                    lexema += c
                    c = prox_char()
                    if c == 'e':
                        lexema += c
                        return 'LB_BOOL', lexema
        elif c == 'g':
            c = prox_char()
            if c == 'o':
                lexema += c
                c = prox_char()
                if c == 't':
                    lexema += c
                    c = prox_char()
                    if c == 'o':
                        lexema += c
                        return 'LB_GOTO', lexema
        elif c == 'd':
            c = prox_char()
            if c == 'o':
                lexema += c
                return 'LB_DO', lexema
        if c == 'e':
            c = prox_char()
            if c == 'l':
                lexema += c
                c = prox_char()
                if c == 's':
                    lexema += c
                    c = prox_char()
                    if c == 'e':
                        lexema += c
                        return 'LB_ELSE', lexema
        elif c == 'w':
            c = prox_char()
            if c == 'h':
                lexema += c
                c = prox_char()
                if c == 'i':
                    lexema += c
                    c = prox_char()
                    if c == 'l':
                        lexema += c
                        c = prox_char()
                        if c == 'e':
                            lexema += c
                            return 'LB_WHILE', lexema
        elif c == 'r':
            c = prox_char()
            if c == 'e':
                lexema += c
                c = prox_char()
                if c == 't':
                    lexema += c
                    c = prox_char()
                    if c == 'u':
                        lexema += c
                        c = prox_char()
                        if c == 'r':
                            lexema += c
                            c = prox_char()
                            if c == 'n':
                                lexema += c
                                return 'LB_RETURN', lexema
        elif c == 'f':
            c = prox_char()
            if c == 'a':
                lexema += c
                c = prox_char()
                if c == 'l':
                    lexema += c
                    c = prox_char()
                    if c == 's':
                        lexema += c
                        c = prox_char()
                        if c == 'e':
                            lexema += c
                            return 'LB_BOOL', lexema
            if c == 'l':
                lexema += c
                c = prox_char()
                if c == 'o':
                    lexema += c
                    c = prox_char()
                    if c == 'a':
                        lexema += c
                        c = prox_char()
                        if c == 't':
                            lexema += c
                            return 'LB_FLOAT', lexema
            if c == 'o':
                lexema += c
                c = prox_char()
                if c == 'r':
                    lexema += c
                    return 'LB_FOR', lexema
        else:
            while True:
                c = prox_char()
                if letra(c) or c.isdigit() or c in ['_']:
                    lexema += c
                else:
                    break
            volta_um()
            return 'ID', lexema
    elif simbolo(c):
        if c == ',':
            return 'SP_VIRGULA', lexema
        elif c == ';':
            return 'SP_PONTOEVIRGULA', lexema
        elif c == '(':
            return 'SP_ABREPARENTESES', lexema
        elif c == ')':
            return 'SP_FECHAPARENTESES', lexema
        elif c == '[':
            return 'SP_ABRECOLCHETES', lexema
        elif c == ']':
            return 'SP_FECHACOLCHETES', lexema
        elif c == '{':
            return 'SP_ABRECHAVES', lexema
        elif c == '}':
            return 'SP_FECHACHAVES', lexema
        elif c == '+':
            c = prox_char()
            if c == '+':
                lexema += c
                return 'OP_INCREMENTO', lexema
            elif c == '=':
                lexema += c
                return 'OP_ADICAOIGUAL', lexema
            else:
                return 'OP_ADICAO', lexema
        elif c == '-':
            c = prox_char()
            if c == '-':
                lexema += c
                return 'OP_DECREMENTO', lexema
            elif c == '=':
                lexema += c
                return 'OP_SUBTRACAOIGUAL', lexema
            elif c == '>':
                lexema += c
                return 'OP_FLECHA', lexema
            else:
                return 'OP_SUBTRACAO', lexema
        elif c == '*':
            c = prox_char()
            if c == '=':
                lexema += c
                return 'OP_MULTIPLICACAOIGUAL', lexema
            else:
                return 'OP_MULTIPLICACAO', lexema
        elif c == '/':
            c = prox_char()
            if c == '=':
                lexema += c
                return 'OP_DIVISAOIGUAL', lexema
            elif c == '/':
                while c != '\n':
                    c = prox_char()
                return None, None
            else:
                return 'OP_DIVISAO', lexema
        elif c == '%':
            c = prox_char()
            if c == '=':
                lexema += c
                return 'OP_MODULOIGUAL', lexema
            else:
                return 'OP_MODULO', lexema
        elif c == '?':
            return 'OP_TERNARIO', lexema
        elif c == ':':
            return 'OP_DOISPONTOS', lexema
        elif c == '!':
            c = prox_char()
            if c == '=':
                lexema += c
                return 'OP_DIFERENTE', lexema
            else:
                return 'OP_NEGACAO', lexema
        elif c == '&':
            c = prox_char()
            if c == '&':
                lexema += c
                return 'OP_AND', lexema
            else:
                return 'OP_ENDERECO', lexema
        elif c == '.':
            return 'OP_PONTO', lexema
        elif c == '>':
            c = prox_char()
            if c == '=':
                lexema += c
                return 'OP_MENORIGUAL', lexema
            else:
                return 'OP_MENOR', lexema
        elif c == '<':
            c = prox_char()
            if c == '=':
                lexema += c
                return 'OP_MAIORIGUAL', lexema
            else:
                return 'OP_MAIOR', lexema
        elif c == '=':
            c = prox_char()
            if c == '=':
                lexema += c
                return 'OP_IGUALDADE', lexema
            else:
                return 'OP_IGUAL', lexema
        elif c == '|':
            c = prox_char()
            if c == '|':
                lexema += c
                return 'OP_OR', lexema
        elif c == '"':
            c = prox_char()
            while c != '"':
                lexema += c
                c = prox_char()
                if fim():
                    return 'ERRO - String incompleta', lexema
            lexema += c
            return 'LB_STRING', lexema
        elif c == "'":
            c = prox_char()
            lexema += c
            c = prox_char()
            if c == "'":
                lexema += c
                return 'LB_CHAR', lexema
            else:
                return 'ERRO - Char invalido', lexema
    else:
        return 'ERRO - Operador Inválido', c

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Número inválido de argumentos. Use core.py filename.dmais")
        sys.exit()

    arquivoEntrada = open(sys.argv[1], 'r')
    entrada = arquivoEntrada.read()
    arquivoEntrada.close()
    arquivoSaida = open('log-analexo.txt', 'w')

    token = ''
    lexema = ''

    while token != 'FIM':
        token, lexema = analex()
        grava_token(arquivoSaida, token, lexema)
    
    arquivoSaida.close()