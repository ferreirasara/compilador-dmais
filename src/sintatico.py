import lexico
import sys

global arquivoSaida


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


def proximo(_entrada, _contador):
    """
    Obtem o próximo token, retornado pelo analisador léxico
    :param _entrada: arquivo a ser analisado
    :param _contador: posicao no arquivo
    :type _entrada: str
    :type _contador: int
    """
    token = None
    while token is None:
        token, lexema, _contador = lexico.lexico(_entrada, _contador)
    return token, _contador


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
    log(token, nomeFuncao, msg)
    print("ERRO - ", msg+token)
    arquivoSaida.close()
    sys.exit()


def var(_entrada, _token, _contador):
    if _token != 'ID':
        erro(_token, 'var', 'Esperado identificador. Recebido ')
    else:
        log(_token, 'var', 'OK')


def literal(_entrada, _token, _contador):
    if _token not in ['LB_INT', 'LB_FLOAT', 'LB_CHAR', 'LB_STRING']:
        erro(_token, 'literal', 'Esperado um literal (int, float, char ou string). Recebido ')
    else:
        log(_token, 'literal', 'OK')


def exp_simples(_entrada, _token, _contador):
    if _token == 'SP_ABREPARENTESES':
        log(_token, 'exp_simples', 'OK')
        token, contador = proximo(_entrada, _contador)
        exp(_entrada, token, contador)
        token, contador = proximo(_entrada, contador)
        if token != 'SP_FECHAPARENTESES':
            erro(token, 'exp_simples', 'Esperado ). Recebido ')
        else:
            log(token, 'exp_simples', 'OK')
    elif _token == 'ID':
        var(_entrada, _token, _contador)
    elif _token in ['LB_INT', 'LB_FLOAT', 'LB_CHAR', 'LB_STRING']:
        literal(_entrada, _token, _contador)
    else:
        erro(_token, 'exp_simples', 'Esperado (exp), identificador ou literal. Recebido ')


def op_mult(_entrada, _token, _contador):
    if _token not in ['OP_MULTIPLICACAOIGUAL', 'OP_MULTIPLICACAO', 'OP_DIVISAOIGUAL', 'OP_DIVISAO', 'OP_MODULOIGUAL',
                      'OP_MODULO']:
        erro(_token, 'op_mult', 'Esperado um dos operadores: *, *=, /, /=, %, %=. Recebido ')
    else:
        log(_token, 'op_mult', 'OK')


def exp_mult1(_entrada, _token, _contador):
    if _token in ['LB_INT', 'LB_FLOAT', 'LB_CHAR', 'LB_STRING', 'ID', 'SP_ABREPARENTESES']:
        op_mult(_entrada, _token, _contador)
        token, contador = proximo(_entrada, _contador)
        exp_mult(_entrada, token, contador)


def exp_mult(_entrada, _token, _contador):
    if _token in ['LB_INT', 'LB_FLOAT', 'LB_CHAR', 'LB_STRING', 'ID', 'SP_ABREPARENTESES']:
        exp_simples(_entrada, _token, _contador)
        token, contador = proximo(_entrada, _contador)
        exp_mult1(_entrada, token, contador)


def op_soma(_entrada, _token, _contador):
    if _token not in ['OP_SUBTRACAO', 'OP_SUBTRACAOIGUAL', 'OP_ADICAOIGUAL', 'OP_ADICAO']:
        erro(_token, 'op_soma', 'Esperado um dos operadores: +, +=, -, -=. Recebido: ')
    else:
        log(_token, 'op_soma', 'OK')


def exp_soma1(_entrada, _token, _contador):
    if _token in ['LB_INT', 'LB_FLOAT', 'LB_CHAR', 'LB_STRING', 'ID', 'SP_ABREPARENTESES']:
        op_soma(_entrada, _token, _contador)
        token, contador = proximo(_entrada, _contador)
        exp_soma(_entrada, token, contador)


def exp_soma(_entrada, _token, _contador):
    if _token in ['LB_INT', 'LB_FLOAT', 'LB_CHAR', 'LB_STRING', 'ID', 'SP_ABREPARENTESES']:
        exp_mult(_entrada, _token, _contador)
        token, contador = proximo(_entrada, _contador)
        exp_soma1(_entrada, token, contador)


def op_relac(_entrada, _token, _contador):
    if _token not in ['OP_MAIORIGUAL', 'OP_MAIOR', 'OP_MENORIGUAL', 'OP_MENOR', 'OP_IGUALDADE', 'OP_DIFERENTE']:
        erro(_token, 'op_relac', 'Esperado um dos operadores: <=, <, >, >=, ==, !=, <>. Recebido ')
    else:
        log(_token, 'op_relac', 'OK')


def exp1(_entrada, _token, _contador):
    if _token in ['LB_INT', 'LB_FLOAT', 'LB_CHAR', 'LB_STRING', 'ID', 'SP_ABREPARENTESES']:
        op_relac(_entrada, _token, _contador)
        token, contador = proximo(_entrada, _contador)
        exp_soma(_entrada, token, contador)


def exp(_entrada, _token, _contador):
    if _token in ['LB_INT', 'LB_FLOAT', 'LB_CHAR', 'LB_STRING', 'ID', 'SP_ABREPARENTESES']:
        exp_soma(_entrada, _token, _contador)
        token, contador = proximo(_entrada, _contador)
        exp1(_entrada, token, contador)


def com_repeticao(_entrada, _token, _contador):
    if _token == 'PR_WHILE':
        log(_token, 'com_repeticao', 'OK')
        token, contador = proximo(_entrada, _contador)
        exp(_entrada, token, contador)
        token, contador = proximo(_entrada, contador)
        if token == 'PR_DO':
            log(token, 'com_repeticao', 'OK')
            token, contador = proximo(_entrada, contador)
            bloco(_entrada, token, contador)
            token, contador = proximo(_entrada, contador)
            if token == 'PR_LOOP':
                log(token, 'com_repeticao', 'OK')
                token, contador = proximo(_entrada, contador)
                if token != 'SP_PONTOEVIRGULA':
                    erro(token, 'com_repeticao', 'Esperado ;. Recebido ')
                else:
                    log(token, 'com_repeticao', 'OK')
            else:
                erro(token, 'com_repeticao', 'Esperado loop. Recebido ')
        else:
            erro(token, 'com_repeticao', 'Esperado do. Recebido ')
    else:
        erro(_token, 'com_repeticao', 'Esperado while. Recebido ')


def com_selecao1(_entrada, _token, _contador):
    if _token == 'PR_ELSE':
        log(_token, 'com_selecao1', 'OK')
        token, contador = proximo(_entrada, _contador)
        bloco(_entrada, token, contador)
        token, contador = proximo(_entrada, contador)
        if token == 'PR_ENDIF':
            log(token, 'com_selecao1', 'OK')
            token, contador = proximo(_entrada, contador)
            if token != 'SP_PONTOEVIRGULA':
                erro(token, 'com_selecao1', 'Esperado ;. Recebido ')
            else:
                log(token, 'com_selecao1', 'OK')
        else:
            erro(token, 'com_selecao1', 'Esperado end-if. Recebido ')
    elif _token == 'PR_ENDIF':
        log(_token, 'com_selecao1', 'OK')
        token, contador = proximo(_entrada, _contador)
        if token != 'SP_PONTOEVIRGULA':
            erro(token, 'com_selecao1', 'Esperado ;. Recebido ')
        else:
            log(token, 'com_selecao1', 'OK')
    else:
        erro(_token, 'com_selecao1', 'Esperado end-if. Recebido ')


def com_selecao(_entrada, _token, _contador):
    if _token == 'PR_IF':
        log(_token, 'com_selecao', 'OK')
        token, contador = proximo(_entrada, _contador)
        exp(_entrada, token, contador)
        token, contador = proximo(_entrada, contador)
        if token == 'SP_FECHAPARENTESES':
            log(token, 'com_selecao', 'OK')
            token, contador = proximo(_entrada, contador)
            if token == 'PR_THEN':
                log(token, 'com_selecao', 'OK')
                token, contador = proximo(_entrada, contador)
                bloco(_entrada, token, contador)
                token, contador = proximo(_entrada, contador)
                com_selecao1(_entrada, token, contador)


def com_escrita(_entrada, _token, _contador):
    if _token == 'PR_PRINT' or _token == 'PR_PRINTLN':
        log(_token, 'com_escrita', 'OK')
        token, contador = proximo(_entrada, _contador)
        if token == 'SP_ABREPARENTESES':
            log(token, 'com_escrita', 'OK')
            token, contador = proximo(_entrada, contador)
            exp(_entrada, token, contador)
            token, contador = proximo(_entrada, contador)
            if token == 'SP_FECHAPARENTESES':
                log(token, 'com_escrita', 'OK')
                token, contador = proximo(_entrada, contador)
                if token != 'SP_PONTOEVIRGULA':
                    erro(token, 'com_escrita', 'Esperado ;. Recebido ')
                else:
                    log(token, 'com_escrita', 'OK')
            else:
                erro(token, 'com_escrita', 'Esperado ). Recebido ')
        else:
            erro(token, 'com_escrita', 'Esperado (. Recebido ')
    else:
        erro(_token, 'com_escrita', 'Esperado print ou println. Recebido ')


def com_leitura(_entrada, _token, _contador):
    if _token == 'PR_SCAN' or _token == 'PR_SCANLN':
        log(_token, 'com_leitura', 'OK')
        token, contador = proximo(_entrada, _contador)
        if token == 'SP_ABREPARENTESES':
            log(token, 'com_leitura', 'OK')
            token, contador = proximo(_entrada, contador)
            var(_entrada, token, contador)
            token, contador = proximo(_entrada, contador)
            if token == 'SP_FECHAPARENTESES':
                log(token, 'com_leitura', 'OK')
                token, contador = proximo(_entrada, contador)
                if token != 'SP_PONTOEVIRGULA':
                    erro(token, 'com_leitura', 'Esperado ;. Recebido ')
                else:
                    log(token, 'com_leitura', 'OK')
            else:
                erro(token, 'com_leitura', 'Esperado ). Recebido ')
        else:
            erro(token, 'com_leitura', 'Esperado (. Recebido ')
    else:
        erro(_token, 'com_leitura', 'Esperado scan ou scanln. Recebido ')


def com_atrib(_entrada, _token, _contador):
    if _token == 'PR_VAR':
        log(_token, 'com_atrib', 'OK')
        token, contador = proximo(_entrada, _contador)
        if token == 'OP_IGUAL':
            log(token, 'com_atrib', 'OK')
            token, contador = proximo(_entrada, contador)
            exp(_entrada, token, contador)
            token, contador = proximo(_entrada, contador)
            if token != 'SP_PONTOEVIRGULA':
                erro(token, 'com_atrib', 'Esperado ;. Recebido ')
            else:
                log(token, 'com_atrib', 'OK')


def comando(_entrada, _token, _contador):
    if _token == 'PR_VAR':
        decl_var(_entrada, _token, _contador)
    elif _token == 'PR_IF':
        com_selecao(_entrada, _token, _contador)
    elif _token == 'PR_WHILE':
        com_repeticao(_entrada, _token, _contador)
    elif _token == 'PR_SCAN' or _token == 'PR_SCANLN':
        com_leitura(_entrada, _token, _contador)
    elif _token == 'PR_PRINT' or _token == 'PR_PRINTLN':
        com_escrita(_entrada, _token, _contador)
    else:
        com_atrib(_entrada, _token, _contador)


def lista_com(_entrada, _token, _contador):
    if _token in ['PR_SCAN', 'PR_SCANLN', 'PR_PRINT', 'PR_PRINTLN', 'PR_IF', 'PR_WHILE', 'PR_VAR', 'PR_ID', 'PR_ENDIF']:
        comando(_entrada, _token, _contador)
        token, contador = proximo(_entrada, _contador)
        lista_com(_entrada, token, contador)


def bloco(_entrada, _token, _contador):
    if _token in ['PR_SCAN', 'PR_SCANLN', 'PR_PRINT', 'PR_PRINTLN', 'PR_IF', 'PR_WHILE', 'PR_VAR', 'PR_ID', 'PR_ENDIF']:
        lista_com(_entrada, _token, _contador)


def espec_tipo(_entrada, _token, _contador):
    if _token not in ['PR_INT', 'PR_FLOAT', 'PR_CHAR']:
        erro(_token, 'espec_tipo', 'Esperado um tipo de variavel (int, float ou char). Recebido ')
    else:
        log(_token, 'espec_tipo', 'OK')


def decl_main(_entrada, _token, _contador):
    if _token == 'PR_MAIN':
        log(_token, 'decl_main', 'OK')
        token, contador = proximo(_entrada, _contador)
        if token == 'SP_ABREPARENTESES':
            log(token, 'decl_main', 'OK')
            token, contador = proximo(_entrada, contador)
            if token == 'SP_FECHAPARENTESES':
                log(token, 'decl_main', 'OK')
                token, contador = proximo(_entrada, contador)
                bloco(_entrada, token, contador)
            else:
                erro(token, 'decl_main', 'Esperado ). Recebido ')
        else:
            erro(token, 'decl_main', 'Esperado (. Recebido ')
    else:
        erro(_token, 'decl_main', 'Esperado main. Recebido ')


def decl_var(_entrada, _token, _contador):
    if _token == 'PR_VAR':
        log(_token, 'decl_var', 'OK')
        token, contador = proximo(_entrada, _contador)
        espec_tipo(_entrada, token, contador)
        token, contador = proximo(_entrada, contador)
        var(_entrada, token, contador)


def decl(_entrada, _token, _contador):
    if _token == 'PR_VAR':
        decl_var(_entrada, _token, _contador)
    elif _token == 'PR_MAIN':
        decl_main(_entrada, _token, _contador)
    else:
        erro(_token, 'decl', 'Esperado var ou main. Recebido ')


def lista_decl1(_entrada, _token, _contador):
    if _token in ['PR_VAR', 'PR_MAIN']:
        decl(_entrada, _token, _contador)


def lista_decl(_entrada, _token, _contador):
    if _token in ['PR_VAR', 'PR_MAIN']:
        decl(_entrada, _token, _contador)
        token, contador = proximo(_entrada, _contador)
        lista_decl1(_entrada, token, contador)


def programa(_entrada, _token, _contador):
    if _token in ['PR_VAR', 'PR_MAIN']:
        lista_decl(_entrada, _token, _contador)


def sintatico(entrada):
    global arquivoSaida
    arquivoSaida = open('log-sintatico.txt', 'w')
    contador = -1
    token, contador = proximo(entrada, contador)
    programa(entrada, token, contador)
    print('Análise sintática OK.')

    arquivoSaida.close()
