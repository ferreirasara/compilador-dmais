def grava_token(arquivo, token, lexema):
    """
    Grava o token e o lexema no arquivo.
    :param arquivo: arquivo no qual será gravado o token
    :param token: token a ser gravado
    :param lexema: lexema a ser gravado
    :type arquivo: _io.TextIO
    :type token: str
    :type lexema: str
    """
    if token is not None and lexema is not None:
        arquivo.write(str(token).ljust(20, ' '))
        arquivo.write(' | ')
        arquivo.write(str(lexema))
        arquivo.write('\n')
        # print(str(token).ljust(20, ' '), ' | ', str(lexema))


def volta_um(contador):
    """
    Volta somente um caracter
    :param contador: inteiro utilizado para determinar uma posição na string
    :type contador: int
    :return: retorna o novo contador
    :rtype: int
    """
    contador -= 1
    return contador


def volta(contador, quantidade):
    """
    Volta uma determinada quantidade de caracteres
    :param contador: inteiro utilizado para determinar uma posição na string
    :param quantidade: inteiro utilizado para determinar a nova posição na string
    :type contador: int
    :type quantidade: int
    :return: retorna o novo contador
    :rtype: int
    """
    return contador - quantidade


def prox_char(entrada, contador):
    """
    Retorna o próximo caracter do arquivo
    :param entrada: string que representa o arquivo que está sendo analisado
    :param contador: inteiro utilizado para determinar a nova posição na string
    :type entrada: str
    :type contador: int
    :return: retorna o proximo caracter da string
    :rtype: str
    """
    if contador < len(entrada) - 1:
        contador += 1
    return entrada[contador], contador


def letra(caracter):
    """
    Verifica se o caracter é uma letra, maiúscula ou minúscula
    :param caracter: caracter atual
    :type caracter: str
    :return: retorna se o caracter é uma letra
    :rtype: bool
    """
    return ord(caracter) in range(65, 91) or ord(caracter) in range(97, 123)


def simbolo(caracter):
    """
    Verifica se o caracter é um dos símbolos permitidos na linguagem
    :param caracter: caracter atual
    :type caracter: str
    :return: retorna se o caracter é um símbolo
    :rtype: bool
    """
    return ord(caracter) in [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 58, 59, 60, 61, 62, 63, 91, 93,
                             95, 123, 124, 125]


def fim(entrada, contador):
    """
    Verifica o fim do arquivo
    :param entrada: string que representa o arquivo que está sendo analisado
    :param contador: inteiro utilizado para determinar a nova posição na string
    :type entrada: str
    :type contador: int
    :return: retorna se é o final da string
    :rtype: bool
    """
    if contador < len(entrada) - 1:
        return False
    else:
        return True
