import sys
import util
import lexico
import sintatico


if __name__ == '__main__':
    arquivoEntrada = open('teste.dmais', 'r')
    entrada = arquivoEntrada.read()
    arquivoEntrada.close()
    sintatico.sintatico(entrada)
    # if len(sys.argv) != 3:
    #     print("Número inválido de argumentos. Use python core.py -[opcao] [arquivo]")
    #     print("python core.py -l >> faz a análise léxica do arquivo")
    #     print("python core.py -s >> faz a análise sintática do arquivo")
    #     sys.exit()
    #
    # arquivoEntrada = open(sys.argv[2], 'r')
    # entrada = arquivoEntrada.read()
    # arquivoEntrada.close()
    #
    # if sys.argv[1] == '-l':
    #     arquivoSaida = open('log-lexico.txt', 'w')
    #
    #     contador = -1
    #     token = ''
    #     lexema = ''
    #
    #     while token != 'FIM' and token != 'ERRO':
    #         token, lexema, contador = lexico.lexico(entrada, contador)
    #         util.grava_token(arquivoSaida, token, lexema)
    #
    #     arquivoSaida.close()
    #
    # elif sys.argv[1] == '-s':
    #     sintatico.sintatico(entrada)

    # else:
    #     print("Número inválido de argumentos. Use python core.py -[opcao] [arquivo]")
    #     print("python core.py -l >> faz a análise léxica do arquivo")
    #     print("python core.py -s >> faz a análise sintática do arquivo")
    #     sys.exit()
