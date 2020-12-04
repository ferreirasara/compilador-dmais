import lexico
import sys

arquivoSaida = open('log-sintatico.txt', 'w')
tabelaDeSimbolos = []


# tabelaDeSimbolos = ['a', 'var', 'int', True (declarada), False (não inicializada), '' (quando for removida)]

def consultarSimbolo(TS, identificador):
    for i in range(len(TS)):
        if TS[i][0] == identificador:
            return i
    return -1


def removerSimbolo(TS, identificador):
    index = consultarSimbolo(TS, identificador)
    if index != -1:
        TS[index][5] = 'removida'
        return True
    return False


def adicionarSimbolo(TS, identificador, categoria, tipo='?'):
    if consultarSimbolo(TS, identificador) == -1:
        TS.append([identificador, tipo, categoria, True, False, 'nao removida'])
        return True
    return False


def modificarTipoSimbolo(TS, identificador, tipo):
    index = consultarSimbolo(TS, identificador)
    if index != -1:
        TS[index][1] = tipo
        return True
    return False


def modificarInicializadaSimbolo(TS, identificador, inicializada):
    index = consultarSimbolo(TS, identificador)
    if index != -1:
        TS[index][4] = inicializada
        return True
    return False


def log(token, nomeFuncao, msg):
    """
    Grava o log do analisador sintático
    :param token: token atual, retornado pelo analisador léxico
    :param nomeFuncao: nome da função que chamou o log
    :param msg: mesagem a ser gravada
    :type token: str
    :type nomeFuncao: str
    :type msg: str
    """
    global arquivoSaida
    arquivoSaida.write(token)
    arquivoSaida.write('\t')
    arquivoSaida.write(nomeFuncao)
    arquivoSaida.write('\t')
    arquivoSaida.write(msg)
    arquivoSaida.write('\n')


def proximo(entrada, contador):
    """
    Obtem o próximo token, retornado pelo analisador léxico
    :param entrada: arquivo a ser analisado
    :param contador: posicao no arquivo
    :type entrada: str
    :type contador: int
    """
    token = None
    lexema = ''
    while token is None:
        token, lexema, contador = lexico.lexico(entrada, contador)
    return token, lexema, contador


def erro(token, nomeFuncao, msg):
    """
    Imprime uma mensagem de erro, faz o log, e sai do analisador
    :param token: token atual, retornado pelo analisador léxico
    :param nomeFuncao: nome da função que chamou o log
    :param msg: mensagem de erro
    :type nomeFuncao: str
    :type token: str
    :type msg: str
    """
    global arquivoSaida
    log(token, nomeFuncao, msg + token)
    print("ERRO - ", msg + token)
    arquivoSaida.close()
    sys.exit()


def var(entrada, lexema, token, contador):
    if token != 'ID':
        erro(token, 'var', 'Esperado identificador. Recebido ')
    else:
        log(token, 'var', 'OK')
        if not adicionarSimbolo(tabelaDeSimbolos, lexema, 'var'):
            log(token, 'var', 'Idenfiticador já existente.')


def literal(entrada, token, lexema, contador):
    if token not in ['LB_INT', 'LB_FLOAT', 'LB_CHAR', 'LB_STRING']:
        erro(token, 'literal', 'Esperado um literal (int, float, char ou string). Recebido ')
    else:
        log(token, 'literal', 'OK')


def exp_simples(entrada, token, lexema, contador):
    if token == 'SP_ABREPARENTESES':
        log(token, 'exp_simples', 'OK')
        token, lexema, contador = proximo(entrada, contador)
        exp(entrada, token, lexema, contador)
        token, lexema, contador = proximo(entrada, contador)
        if token != 'SP_FECHAPARENTESES':
            erro(token, 'exp_simples', 'Esperado ). Recebido ')
        else:
            log(token, 'exp_simples', 'OK')
    elif token == 'ID':
        var(entrada, token, lexema, contador)
    elif token in ['LB_INT', 'LB_FLOAT', 'LB_CHAR', 'LB_STRING']:
        literal(entrada, token, lexema, contador)
    else:
        erro(token, 'exp_simples', 'Esperado (exp), identificador ou literal. Recebido ')


def op_mult(entrada, token, lexema, contador):
    if token not in ['OP_MULTIPLICACAOIGUAL', 'OP_MULTIPLICACAO', 'OP_DIVISAOIGUAL', 'OP_DIVISAO', 'OP_MODULOIGUAL',
                     'OP_MODULO']:
        erro(token, 'op_mult', 'Esperado um dos operadores: *, *=, /, /=, %, %=. Recebido ')
    else:
        log(token, 'op_mult', 'OK')


def exp_mult1(entrada, token, lexema, contador):
    if token in ['LB_INT', 'LB_FLOAT', 'LB_CHAR', 'LB_STRING', 'ID', 'SP_ABREPARENTESES']:
        op_mult(entrada, token, lexema, contador)
        token, lexema, contador = proximo(entrada, contador)
        exp_mult(entrada, token, lexema, contador)


def exp_mult(entrada, token, lexema, contador):
    if token in ['LB_INT', 'LB_FLOAT', 'LB_CHAR', 'LB_STRING', 'ID', 'SP_ABREPARENTESES']:
        exp_simples(entrada, token, lexema, contador)
        token, lexema, contador = proximo(entrada, contador)
        exp_mult1(entrada, token, lexema, contador)


def op_soma(entrada, token, lexema, contador):
    if token not in ['OP_SUBTRACAO', 'OP_SUBTRACAOIGUAL', 'OP_ADICAOIGUAL', 'OP_ADICAO']:
        erro(token, 'op_soma', 'Esperado um dos operadores: +, +=, -, -=. Recebido: ')
    else:
        log(token, 'op_soma', 'OK')


def exp_soma1(entrada, token, lexema, contador):
    if token in ['LB_INT', 'LB_FLOAT', 'LB_CHAR', 'LB_STRING', 'ID', 'SP_ABREPARENTESES']:
        op_soma(entrada, token, lexema, contador)
        token, lexema, contador = proximo(entrada, contador)
        exp_soma(entrada, token, lexema, contador)


def exp_soma(entrada, token, lexema, contador):
    if token in ['LB_INT', 'LB_FLOAT', 'LB_CHAR', 'LB_STRING', 'ID', 'SP_ABREPARENTESES']:
        exp_mult(entrada, token, lexema, contador)
        token, lexema, contador = proximo(entrada, contador)
        exp_soma1(entrada, token, lexema, contador)


def op_relac(entrada, token, lexema, contador):
    if token not in ['OP_MAIORIGUAL', 'OP_MAIOR', 'OP_MENORIGUAL', 'OP_MENOR', 'OP_IGUALDADE', 'OP_DIFERENTE']:
        erro(token, 'op_relac', 'Esperado um dos operadores: <=, <, >, >=, ==, !=, <>. Recebido ')
    else:
        log(token, 'op_relac', 'OK')


def exp1(entrada, token, lexema, contador):
    if token in ['LB_INT', 'LB_FLOAT', 'LB_CHAR', 'LB_STRING', 'ID', 'SP_ABREPARENTESES']:
        op_relac(entrada, token, lexema, contador)
        token, lexema, contador = proximo(entrada, contador)
        exp_soma(entrada, token, lexema, contador)


def exp(entrada, token, lexema, contador):
    if token in ['LB_INT', 'LB_FLOAT', 'LB_CHAR', 'LB_STRING', 'ID', 'SP_ABREPARENTESES']:
        exp_soma(entrada, token, lexema, contador)
        token, lexema, contador = proximo(entrada, contador)
        exp1(entrada, token, lexema, contador)


def com_repeticao(entrada, token, lexema, contador):
    if token == 'PR_WHILE':
        log(token, 'com_repeticao', 'OK')
        token, lexema, contador = proximo(entrada, contador)
        exp(entrada, token, lexema, contador)
        token, lexema, contador = proximo(entrada, contador)
        if token == 'PR_DO':
            log(token, 'com_repeticao', 'OK')
            token, lexema, contador = proximo(entrada, contador)
            bloco(entrada, token, lexema, contador)
            token, lexema, contador = proximo(entrada, contador)
            if token == 'PR_LOOP':
                log(token, 'com_repeticao', 'OK')
                token, lexema, contador = proximo(entrada, contador)
                if token != 'SP_PONTOEVIRGULA':
                    erro(token, 'com_repeticao', 'Esperado ;. Recebido ')
                else:
                    log(token, 'com_repeticao', 'OK')
            else:
                erro(token, 'com_repeticao', 'Esperado loop. Recebido ')
        else:
            erro(token, 'com_repeticao', 'Esperado do. Recebido ')
    else:
        erro(token, 'com_repeticao', 'Esperado while. Recebido ')


def com_selecao1(entrada, token, lexema, contador):
    if token == 'PR_ELSE':
        log(token, 'com_selecao1', 'OK')
        token, lexema, contador = proximo(entrada, contador)
        bloco(entrada, token, lexema, contador)
        token, lexema, contador = proximo(entrada, contador)
        if token == 'PR_ENDIF':
            log(token, 'com_selecao1', 'OK')
            token, lexema, contador = proximo(entrada, contador)
            if token != 'SP_PONTOEVIRGULA':
                erro(token, 'com_selecao1', 'Esperado ;. Recebido ')
            else:
                log(token, 'com_selecao1', 'OK')
        else:
            erro(token, 'com_selecao1', 'Esperado end-if. Recebido ')
    elif token == 'PR_ENDIF':
        log(token, 'com_selecao1', 'OK')
        token, lexema, contador = proximo(entrada, contador)
        if token != 'SP_PONTOEVIRGULA':
            erro(token, 'com_selecao1', 'Esperado ;. Recebido ')
        else:
            log(token, 'com_selecao1', 'OK')
    else:
        erro(token, 'com_selecao1', 'Esperado end-if. Recebido ')


def com_selecao(entrada, token, lexema, contador):
    if token == 'PR_IF':
        log(token, 'com_selecao', 'OK')
        token, lexema, contador = proximo(entrada, contador)
        exp(entrada, token, lexema, contador)
        token, lexema, contador = proximo(entrada, contador)
        if token == 'SP_FECHAPARENTESES':
            log(token, 'com_selecao', 'OK')
            token, lexema, contador = proximo(entrada, contador)
            if token == 'PR_THEN':
                log(token, 'com_selecao', 'OK')
                token, lexema, contador = proximo(entrada, contador)
                bloco(entrada, token, lexema, contador)
                token, lexema, contador = proximo(entrada, contador)
                com_selecao1(entrada, token, lexema, contador)


def com_escrita(entrada, token, lexema, contador):
    if token == 'PR_PRINT' or token == 'PR_PRINTLN':
        log(token, 'com_escrita', 'OK')
        token, lexema, contador = proximo(entrada, contador)
        if token == 'SP_ABREPARENTESES':
            log(token, 'com_escrita', 'OK')
            token, lexema, contador = proximo(entrada, contador)
            exp(entrada, token, lexema, contador)
            token, lexema, contador = proximo(entrada, contador)
            if token == 'SP_FECHAPARENTESES':
                log(token, 'com_escrita', 'OK')
                token, lexema, contador = proximo(entrada, contador)
                if token != 'SP_PONTOEVIRGULA':
                    erro(token, 'com_escrita', 'Esperado ;. Recebido ')
                else:
                    log(token, 'com_escrita', 'OK')
            else:
                erro(token, 'com_escrita', 'Esperado ). Recebido ')
        else:
            erro(token, 'com_escrita', 'Esperado (. Recebido ')
    else:
        erro(token, 'com_escrita', 'Esperado print ou println. Recebido ')


def com_leitura(entrada, token, lexema, contador):
    if token == 'PR_SCAN' or token == 'PR_SCANLN':
        log(token, 'com_leitura', 'OK')
        token, lexema, contador = proximo(entrada, contador)
        if token == 'SP_ABREPARENTESES':
            log(token, 'com_leitura', 'OK')
            token, lexema, contador = proximo(entrada, contador)
            var(entrada, token, lexema, contador)
            token, lexema, contador = proximo(entrada, contador)
            if token == 'SP_FECHAPARENTESES':
                log(token, 'com_leitura', 'OK')
                token, lexema, contador = proximo(entrada, contador)
                if token != 'SP_PONTOEVIRGULA':
                    erro(token, 'com_leitura', 'Esperado ;. Recebido ')
                else:
                    log(token, 'com_leitura', 'OK')
            else:
                erro(token, 'com_leitura', 'Esperado ). Recebido ')
        else:
            erro(token, 'com_leitura', 'Esperado (. Recebido ')
    else:
        erro(token, 'com_leitura', 'Esperado scan ou scanln. Recebido ')


def com_atrib(entrada, token, lexema, contador):
    if token == 'PR_VAR':
        log(token, 'com_atrib', 'OK')
        token, lexema, contador = proximo(entrada, contador)
        if token == 'OP_IGUAL':
            log(token, 'com_atrib', 'OK')
            token, lexema, contador = proximo(entrada, contador)
            exp(entrada, token, lexema, contador)
            token, lexema, contador = proximo(entrada, contador)
            if token != 'SP_PONTOEVIRGULA':
                erro(token, 'com_atrib', 'Esperado ;. Recebido ')
            else:
                log(token, 'com_atrib', 'OK')


def comando(entrada, token, lexema, contador):
    if token == 'PR_VAR':
        decl_var(entrada, token, lexema, contador)
    elif token == 'PR_IF':
        com_selecao(entrada, token, lexema, contador)
    elif token == 'PR_WHILE':
        com_repeticao(entrada, token, lexema, contador)
    elif token == 'PR_SCAN' or token == 'PR_SCANLN':
        com_leitura(entrada, token, lexema, contador)
    elif token == 'PR_PRINT' or token == 'PR_PRINTLN':
        com_escrita(entrada, token, lexema, contador)
    else:
        com_atrib(entrada, token, lexema, contador)


def lista_com(entrada, token, lexema, contador):
    if token in ['PR_SCAN', 'PR_SCANLN', 'PR_PRINT', 'PR_PRINTLN', 'PR_IF', 'PR_WHILE', 'PR_VAR', 'PR_ID', 'PR_ENDIF']:
        comando(entrada, token, lexema, contador)
        token, lexema, contador = proximo(entrada, contador)
        lista_com(entrada, token, lexema, contador)


def bloco(entrada, token, lexema, contador):
    if token in ['PR_SCAN', 'PR_SCANLN', 'PR_PRINT', 'PR_PRINTLN', 'PR_IF', 'PR_WHILE', 'PR_VAR', 'PR_ID', 'PR_ENDIF']:
        lista_com(entrada, token, lexema, contador)


def espec_tipo(entrada, token, lexema, contador):
    if token not in ['PR_INT', 'PR_FLOAT', 'PR_CHAR']:
        erro(token, 'espec_tipo', 'Esperado um tipo de variavel (int, float ou char). Recebido ')
    else:
        log(token, 'espec_tipo', 'OK')


def decl_main(entrada, token, lexema, contador):
    if token == 'PR_MAIN':
        log(token, 'decl_main', 'OK')
        token, lexema, contador = proximo(entrada, contador)
        if token == 'SP_ABREPARENTESES':
            log(token, 'decl_main', 'OK')
            token, lexema, contador = proximo(entrada, contador)
            if token == 'SP_FECHAPARENTESES':
                log(token, 'decl_main', 'OK')
                token, lexema, contador = proximo(entrada, contador)
                bloco(entrada, token, lexema, contador)
            else:
                erro(token, 'decl_main', 'Esperado ). Recebido ')
        else:
            erro(token, 'decl_main', 'Esperado (. Recebido ')
    else:
        erro(token, 'decl_main', 'Esperado main. Recebido ')


def decl_var(entrada, token, lexema, contador):
    if token == 'PR_VAR':
        log(token, 'decl_var', 'OK')
        token, lexema, contador = proximo(entrada, contador)
        espec_tipo(entrada, token, lexema, contador)
        token, lexema, contador = proximo(entrada, contador)
        var(entrada, token, lexema, contador)


def decl(entrada, token, lexema, contador):
    if token == 'PR_VAR':
        decl_var(entrada, token, lexema, contador)
    elif token == 'PR_MAIN':
        decl_main(entrada, token, lexema, contador)
    else:
        erro(token, 'decl', 'Esperado var ou main. Recebido ')


def lista_decl1(entrada, token, lexema, contador):
    if token in ['PR_VAR', 'PR_MAIN']:
        decl(entrada, token, lexema, contador)


def lista_decl(entrada, token, lexema, contador):
    if token in ['PR_VAR', 'PR_MAIN']:
        decl(entrada, token, lexema, contador)
        token, lexema, contador = proximo(entrada, contador)
        lista_decl1(entrada, token, lexema, contador)


def programa(entrada, token, lexema, contador):
    if token in ['PR_VAR', 'PR_MAIN']:
        lista_decl(entrada, token, lexema, contador)


def sintatico(entrada):
    global arquivoSaida
    arquivoSaida = open('log-sintatico.txt', 'w')
    contador = -1
    token, lexema, contador = proximo(entrada, contador)
    programa(entrada, token, lexema, contador)
    print(tabelaDeSimbolos)
    print('Análise sintática OK.')

    arquivoSaida.close()
