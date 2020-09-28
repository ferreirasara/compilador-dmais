import util


def lexico(entrada, contador):
    """
    Analisador Léxico
    :type entrada: str
    :type contador: int
    :returns retorna uma tupla com token, lexema e contador
    :rtype: (str, str, int)
    """
    if util.fim(entrada, contador):
        return 'FIM', None, contador

    c, contador = util.prox_char(entrada, contador)
    lexema = c

    if c.isdigit():
        while True:  # Enquanto for um digito, incrementa o lexema
            c, contador = util.prox_char(entrada, contador)
            if c.isdigit():
                lexema += c
            else:
                break
        if c == '.':  # Caso possua ponto, é um float
            lexema += c
            c, contador = util.prox_char(entrada, contador)
            if not (c.isdigit()):  # Caso não exista um digito depois do ponto, é um erro
                lexema += c
                return 'ERRO', 'Número real inválido: ' + lexema, contador
            else:
                lexema += c
                while True:  # Enquanto for um digito, incrementa o lexema
                    c, contador = util.prox_char(entrada, contador)
                    if c.isdigit():
                        lexema += c
                    else:
                        break
                contador = util.volta_um(contador)
                return 'LB_FLOAT', lexema, contador
        else:  # Se acabaram os digitos retorna um inteiro
            contador = util.volta_um(contador)
            return 'LB_INT', lexema, contador
    elif c in ['\t', '\n', ' ']:
        return None, None, contador
    elif util.letra(c):
        if c == 'v':
            c, contador = util.prox_char(entrada, contador)
            if c == 'o':
                lexema += c
                c, contador = util.prox_char(entrada, contador)
                if c == 'i':
                    lexema += c
                    c, contador = util.prox_char(entrada, contador)
                    if c == 'd':
                        lexema += c
                        c, contador = util.prox_char(entrada, contador)
                        if c == ' ':
                            contador = util.volta_um(contador)
                            return 'LB_VOID', lexema, contador
                        else:
                            lexema = lexema[:-3]
                            contador = util.volta(contador, 4)
                    else:
                        lexema = lexema[:-2]
                        contador = util.volta(contador, 3)
                else:
                    lexema = lexema[:-1]
                    contador = util.volta(contador, 2)
            else:
                contador = util.volta_um(contador)
        elif c == 'i':
            c, contador = util.prox_char(entrada, contador)
            if c == 'n':
                lexema += c
                c, contador = util.prox_char(entrada, contador)
                if c == 't':
                    lexema += c
                    c, contador = util.prox_char(entrada, contador)
                    if c == ' ':
                        contador = util.volta_um(contador)
                        return 'LB_INT', lexema, contador
                    else:
                        lexema = lexema[:-2]
                        contador = util.volta(contador, 3)
                else:
                    lexema = lexema[:-1]
                    contador = util.volta(contador, 2)
            elif c == 'f':
                lexema += c
                c, contador = util.prox_char(entrada, contador)
                if c == ' ':
                    contador = util.volta_um(contador)
                    return 'LB_IF', lexema, contador
                else:
                    lexema = lexema[:-1]
                    contador = util.volta(contador, 2)
            else:
                contador = util.volta_um(contador)
        elif c == 'c':
            c, contador = util.prox_char(entrada, contador)
            if c == 'h':
                lexema += c
                c, contador = util.prox_char(entrada, contador)
                if c == 'a':
                    lexema += c
                    c, contador = util.prox_char(entrada, contador)
                    if c == 'r':
                        lexema += c
                        c, contador = util.prox_char(entrada, contador)
                        if c == ' ':
                            contador = util.volta_um(contador)
                            return 'LB_CHAR', lexema, contador
                        else:
                            lexema = lexema[:-3]
                            contador = util.volta(contador, 4)
                    else:
                        lexema = lexema[:-2]
                        contador = util.volta(contador, 3)
                else:
                    lexema = lexema[:-1]
                    contador = util.volta(contador, 2)
            elif c == 'o':
                lexema += c
                c, contador = util.prox_char(entrada, contador)
                if c == 'n':
                    lexema += c
                    c, contador = util.prox_char(entrada, contador)
                    if c == 't':
                        lexema += c
                        c, contador = util.prox_char(entrada, contador)
                        if c == 'i':
                            lexema += c
                            c, contador = util.prox_char(entrada, contador)
                            if c == 'n':
                                lexema += c
                                c, contador = util.prox_char(entrada, contador)
                                if c == 'u':
                                    lexema += c
                                    c, contador = util.prox_char(entrada, contador)
                                    if c == 'e':
                                        lexema += c
                                        c, contador = util.prox_char(entrada, contador)
                                        if c == ' ':
                                            contador = util.volta_um(contador)
                                            return 'LB_CONTINUE', lexema, contador
                                        else:
                                            lexema = lexema[:-7]
                                            contador = util.volta(contador, 8)
                                    else:
                                        lexema = lexema[:-6]
                                        contador = util.volta(contador, 7)
                                else:
                                    lexema = lexema[:-5]
                                    contador = util.volta(contador, 6)
                            else:
                                lexema = lexema[:-4]
                                contador = util.volta(contador, 5)
                        else:
                            lexema = lexema[:-3]
                            contador = util.volta(contador, 4)
                    else:
                        lexema = lexema[:-2]
                        contador = util.volta(contador, 3)
                else:
                    lexema = lexema[:-1]
                    contador = util.volta(contador, 2)
            else:
                contador = util.volta_um(contador)
        elif c == 'b':
            c, contador = util.prox_char(entrada, contador)
            if c == 'o':
                lexema += c
                c, contador = util.prox_char(entrada, contador)
                if c == 'o':
                    lexema += c
                    c, contador = util.prox_char(entrada, contador)
                    if c == 'l':
                        lexema += c
                        c, contador = util.prox_char(entrada, contador)
                        if c == ' ':
                            contador = util.volta_um(contador)
                            return 'LB_BOOL', lexema, contador
                        else:
                            lexema = lexema[:-3]
                            contador = util.volta(contador, 4)
                    else:
                        lexema = lexema[:-2]
                        contador = util.volta(contador, 3)
                else:
                    lexema = lexema[:-1]
                    contador = util.volta(contador, 2)
            elif c == 'r':
                lexema += c
                c, contador = util.prox_char(entrada, contador)
                if c == 'e':
                    lexema += c
                    c, contador = util.prox_char(entrada, contador)
                    if c == 'a':
                        lexema += c
                        c, contador = util.prox_char(entrada, contador)
                        if c == 'k':
                            lexema += c
                            c, contador = util.prox_char(entrada, contador)
                            if c == ' ':
                                contador = util.volta_um(contador)
                                return 'LB_BREAK', lexema, contador
                            else:
                                lexema = lexema[:-4]
                                contador = util.volta(contador, 5)
                        else:
                            lexema = lexema[:-3]
                            contador = util.volta(contador, 4)
                    else:
                        lexema = lexema[:-2]
                        contador = util.volta(contador, 3)
                else:
                    lexema = lexema[:-1]
                    contador = util.volta(contador, 2)
            else:
                contador = util.volta_um(contador)
        elif c == 't':
            c, contador = util.prox_char(entrada, contador)
            if c == 'r':
                lexema += c
                c, contador = util.prox_char(entrada, contador)
                if c == 'u':
                    lexema += c
                    c, contador = util.prox_char(entrada, contador)
                    if c == 'e':
                        lexema += c
                        c, contador = util.prox_char(entrada, contador)
                        if c == ' ':
                            contador = util.volta_um(contador)
                            return 'LB_BOOL', lexema, contador
                        else:
                            lexema = lexema[:-3]
                            contador = util.volta(contador, 4)
                    else:
                        lexema = lexema[:-2]
                        contador = util.volta(contador, 3)
                else:
                    lexema = lexema[:-1]
                    contador = util.volta(contador, 2)
            else:
                contador = util.volta_um(contador)
        elif c == 'g':
            c, contador = util.prox_char(entrada, contador)
            if c == 'o':
                lexema += c
                c, contador = util.prox_char(entrada, contador)
                if c == 't':
                    lexema += c
                    c, contador = util.prox_char(entrada, contador)
                    if c == 'o':
                        lexema += c
                        c, contador = util.prox_char(entrada, contador)
                        if c == ' ':
                            contador = util.volta_um(contador)
                            return 'LB_GOTO', lexema, contador
                        else:
                            lexema = lexema[:-3]
                            contador = util.volta(contador, 4)
                    else:
                        lexema = lexema[:-2]
                        contador = util.volta(contador, 3)
                else:
                    lexema = lexema[:-1]
                    contador = util.volta(contador, 2)
            else:
                contador = util.volta_um(contador)
        elif c == 'd':
            c, contador = util.prox_char(entrada, contador)
            if c == 'o':
                lexema += c
                c, contador = util.prox_char(entrada, contador)
                if c == ' ':
                    contador = util.volta_um(contador)
                    return 'LB_DO', lexema, contador
                else:
                    lexema = lexema[:-1]
                    contador = util.volta(contador, 2)
            else:
                contador = util.volta_um(contador)
        elif c == 'e':
            c, contador = util.prox_char(entrada, contador)
            if c == 'l':
                lexema += c
                c, contador = util.prox_char(entrada, contador)
                if c == 's':
                    lexema += c
                    c, contador = util.prox_char(entrada, contador)
                    if c == 'e':
                        lexema += c
                        c, contador = util.prox_char(entrada, contador)
                        if c == ' ':
                            contador = util.volta_um(contador)
                            return 'LB_ELSE', lexema, contador
                        else:
                            lexema = lexema[:-3]
                            contador = util.volta(contador, 4)
                    else:
                        lexema = lexema[:-2]
                        contador = util.volta(contador, 3)
                else:
                    lexema = lexema[:-1]
                    contador = util.volta(contador, 2)
            else:
                contador = util.volta_um(contador)
        elif c == 'w':
            c, contador = util.prox_char(entrada, contador)
            if c == 'h':
                lexema += c
                c, contador = util.prox_char(entrada, contador)
                if c == 'i':
                    lexema += c
                    c, contador = util.prox_char(entrada, contador)
                    if c == 'l':
                        lexema += c
                        c, contador = util.prox_char(entrada, contador)
                        if c == 'e':
                            lexema += c
                            c, contador = util.prox_char(entrada, contador)
                            if c == ' ':
                                contador = util.volta_um(contador)
                                return 'LB_WHILE', lexema, contador
                            else:
                                lexema = lexema[:-4]
                                contador = util.volta(contador, 5)
                        else:
                            lexema = lexema[:-3]
                            contador = util.volta(contador, 4)
                    else:
                        lexema = lexema[:-2]
                        contador = util.volta(contador, 3)
                else:
                    lexema = lexema[:-1]
                    contador = util.volta(contador, 2)
            else:
                contador = util.volta_um(contador)
        elif c == 'r':
            c, contador = util.prox_char(entrada, contador)
            if c == 'e':
                lexema += c
                c, contador = util.prox_char(entrada, contador)
                if c == 't':
                    lexema += c
                    c, contador = util.prox_char(entrada, contador)
                    if c == 'u':
                        lexema += c
                        c, contador = util.prox_char(entrada, contador)
                        if c == 'r':
                            lexema += c
                            c, contador = util.prox_char(entrada, contador)
                            if c == 'n':
                                lexema += c
                                c, contador = util.prox_char(entrada, contador)
                                if c == ' ':
                                    contador = util.volta_um(contador)
                                    return 'LB_RETURN', lexema, contador
                                else:
                                    lexema = lexema[:-5]
                                    contador = util.volta(contador, 6)
                            else:
                                lexema = lexema[:-4]
                                contador = util.volta(contador, 5)
                        else:
                            lexema = lexema[:-3]
                            contador = util.volta(contador, 4)
                    else:
                        lexema = lexema[:-2]
                        contador = util.volta(contador, 3)
                else:
                    lexema = lexema[:-1]
                    contador = util.volta(contador, 2)
            else:
                contador = util.volta_um(contador)
        elif c == 'f':
            c, contador = util.prox_char(entrada, contador)
            if c == 'a':
                lexema += c
                c, contador = util.prox_char(entrada, contador)
                if c == 'l':
                    lexema += c
                    c, contador = util.prox_char(entrada, contador)
                    if c == 's':
                        lexema += c
                        c, contador = util.prox_char(entrada, contador)
                        if c == 'e':
                            lexema += c
                            c, contador = util.prox_char(entrada, contador)
                            if c == ' ':
                                contador = util.volta_um(contador)
                                return 'LB_BOOL', lexema, contador
                            else:
                                lexema = lexema[:-4]
                                contador = util.volta(contador, 5)
                        else:
                            lexema = lexema[:-3]
                            contador = util.volta(contador, 4)
                    else:
                        lexema = lexema[:-2]
                        contador = util.volta(contador, 3)
                else:
                    lexema = lexema[:-1]
                    contador = util.volta(contador, 2)
            elif c == 'l':
                lexema += c
                c, contador = util.prox_char(entrada, contador)
                if c == 'o':
                    lexema += c
                    c, contador = util.prox_char(entrada, contador)
                    if c == 'a':
                        lexema += c
                        c, contador = util.prox_char(entrada, contador)
                        if c == 't':
                            lexema += c
                            c, contador = util.prox_char(entrada, contador)
                            if c == ' ':
                                contador = util.volta_um(contador)
                                return 'LB_FLOAT', lexema, contador
                            else:
                                lexema = lexema[:-4]
                                contador = util.volta(contador, 5)
                        else:
                            lexema = lexema[:-3]
                            contador = util.volta(contador, 4)
                    else:
                        lexema = lexema[:-2]
                        contador = util.volta(contador, 3)
                else:
                    lexema = lexema[:-1]
                    contador = util.volta(contador, 2)
            elif c == 'o':
                lexema += c
                c, contador = util.prox_char(entrada, contador)
                if c == 'r':
                    lexema += c
                    c, contador = util.prox_char(entrada, contador)
                    if c == ' ':
                        contador = util.volta_um(contador)
                        return 'LB_FOR', lexema, contador
                    else:
                        lexema = lexema[:-2]
                        contador = util.volta(contador, 3)
                else:
                    lexema = lexema[:-1]
                    contador = util.volta(contador, 2)
            else:
                contador = util.volta_um(contador)
        while True:  # Se não é uma palavra reservada, é um identificador
            c, contador = util.prox_char(entrada, contador)
            if util.letra(c) or c.isdigit() or c in ['_', '$']:
                lexema += c
            elif c in [' ', ';', ',', '(', ')']:
                contador = util.volta_um(contador)
                return 'ID', lexema, contador
            else:
                lexema += c
                return 'ERRO', 'Identificador inválido: ' + lexema, contador
    elif util.simbolo(c):
        if c == ',':
            return 'SP_VIRGULA', lexema, contador
        elif c == ';':
            return 'SP_PONTOEVIRGULA', lexema, contador
        elif c == '(':
            return 'SP_ABREPARENTESES', lexema, contador
        elif c == ')':
            return 'SP_FECHAPARENTESES', lexema, contador
        elif c == '[':
            return 'SP_ABRECOLCHETES', lexema, contador
        elif c == ']':
            return 'SP_FECHACOLCHETES', lexema, contador
        elif c == '{':
            return 'SP_ABRECHAVES', lexema, contador
        elif c == '}':
            return 'SP_FECHACHAVES', lexema, contador
        elif c == '+':
            c, contador = util.prox_char(entrada, contador)
            if c == '+':
                lexema += c
                return 'OP_INCREMENTO', lexema, contador
            elif c == '=':
                lexema += c
                return 'OP_ADICAOIGUAL', lexema, contador
            else:
                return 'OP_ADICAO', lexema, contador
        elif c == '-':
            c, contador = util.prox_char(entrada, contador)
            if c == '-':
                lexema += c
                return 'OP_DECREMENTO', lexema, contador
            elif c == '=':
                lexema += c
                return 'OP_SUBTRACAOIGUAL', lexema, contador
            elif c == '>':
                lexema += c
                return 'OP_FLECHA', lexema, contador
            else:
                return 'OP_SUBTRACAO', lexema, contador
        elif c == '*':
            c, contador = util.prox_char(entrada, contador)
            if c == '=':
                lexema += c
                return 'OP_MULTIPLICACAOIGUAL', lexema, contador
            else:
                return 'OP_MULTIPLICACAO', lexema, contador
        elif c == '/':
            c, contador = util.prox_char(entrada, contador)
            if c == '=':
                lexema += c
                return 'OP_DIVISAOIGUAL', lexema, contador
            elif c == '/':
                while c != '\n':
                    c, contador = util.prox_char(entrada, contador)
                return None, None, contador
            else:
                return 'OP_DIVISAO', lexema, contador
        elif c == '%':
            c, contador = util.prox_char(entrada, contador)
            if c == '=':
                lexema += c
                return 'OP_MODULOIGUAL', lexema, contador
            else:
                return 'OP_MODULO', lexema, contador
        elif c == '?':
            return 'OP_TERNARIO', lexema, contador
        elif c == ':':
            return 'OP_DOISPONTOS', lexema, contador
        elif c == '!':
            c, contador = util.prox_char(entrada, contador)
            if c == '=':
                lexema += c
                return 'OP_DIFERENTE', lexema, contador
            else:
                return 'OP_NEGACAO', lexema, contador
        elif c == '&':
            c, contador = util.prox_char(entrada, contador)
            if c == '&':
                lexema += c
                return 'OP_AND', lexema, contador
            else:
                return 'OP_ENDERECO', lexema, contador
        elif c == '.':
            return 'OP_PONTO', lexema, contador
        elif c == '>':
            c, contador = util.prox_char(entrada, contador)
            if c == '=':
                lexema += c
                return 'OP_MAIORIGUAL', lexema, contador
            else:
                return 'OP_MAIOR', lexema, contador
        elif c == '<':
            c, contador = util.prox_char(entrada, contador)
            if c == '=':
                lexema += c
                return 'OP_MENORIGUAL', lexema, contador
            else:
                return 'OP_MENOR', lexema, contador
        elif c == '=':
            c, contador = util.prox_char(entrada, contador)
            if c == '=':
                lexema += c
                return 'OP_IGUALDADE', lexema, contador
            else:
                return 'OP_IGUAL', lexema, contador
        elif c == '|':
            c, contador = util.prox_char(entrada, contador)
            if c == '|':
                lexema += c
                return 'OP_OR', lexema, contador
        elif c == '"':
            c, contador = util.prox_char(entrada, contador)
            while c != '"':
                lexema += c
                c, contador = util.prox_char(entrada, contador)
                if util.fim(entrada, contador):
                    return 'ERRO', 'String incompleta: ' + lexema, contador
            lexema += c
            return 'LB_STRING', lexema, contador
        elif c == "'":
            c, contador = util.prox_char(entrada, contador)
            lexema += c
            c, contador = util.prox_char(entrada, contador)
            if c == "'":
                lexema += c
                return 'LB_CHAR', lexema, contador
            else:
                lexema += c
                return 'ERRO', 'Char inválido: ' + lexema, contador
    else:
        return 'ERRO', 'Operador inválido: ' + c, contador


# if __name__ == '__main__':
#     if len(sys.argv) != 3:
#         print("Número inválido de argumentos. Use python core.py -[opcao] [arquivo]")
#         print("python core.py -l >> faz a análise léxica do arquivo")
#         print("python core.py -s >> faz a análise sintática do arquivo")
#         sys.exit()
#
#     arquivoEntrada = open(sys.argv[2], 'r')
#     entrada = arquivoEntrada.read()
#     arquivoEntrada.close()
#
#     if sys.argv[1] == '-l':
#         arquivoSaida = open('log-lexico.txt', 'w')
#
#         contador = 0
#         token = ''
#         lexema = ''
#
#         while token != 'FIM' and token != 'ERRO':
#             token, lexema, contador = lexico(entrada, contador)
#             grava_token(arquivoSaida, token, lexema)
#
#         arquivoSaida.close()

    # elif sys.argv[1] == '-s':
    #     arquivoSaida = open('log-sintatico.txt', 'w')

    #     token = ''
    #     lexema = ''

    #     while token != 'FIM' and token != 'ERRO':
    #         # token, lexema = analex()
    #         grava_token(arquivoSaida, token, lexema)

    #     arquivoSaida.close()

    # else:
    #     print("Número inválido de argumentos. Use python core.py -[opcao] [arquivo]")
    #     print("python core.py -l >> faz a análise léxica do arquivo")
    #     print("python core.py -s >> faz a análise sintática do arquivo")
    #     sys.exit()
