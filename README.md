# compilador-dmais

## Sobre o analisador

Na pasta doc, está toda a parte de documentação. Os arquivos mp são referentes ao manual do programador, e os arquivos mu são referentes ao manual do usuário. A pasta `diagramas-de-transicao-jflap` contém os diagramas com extensão jflap. Na pasta `diagramas-de-transicao-png` estão os diagramas exportados para png.

Na pasta src, está o código do analisador. O arquivo `core.py` é o arquivo principal, e é ele que será executado ao utilizar o analisador. O arquivo `lexico.py` implementa a análise léxica, e o arquivo `sintático.py` implementa a análise sintática. Já o arquivo `util.py`, possui funções úteis, que são utilizadas pelos outros arquivos.

Ao executar o analisador, outros arquivos serão criados, log-lexico.txt e log-sintatico.txt, que contém as informações do log da análise.

## Analisando um arquivo

Para fazer a análise léxica de um arquivo, deve-se utilizar o seguinte comando (na pasta src):

`python core.py -l <arquivo>`

Para fazer a análise sintática de um arquivo, deve-se utilizar o seguinte comando (na pasta src):

`python core.py -s <arquivo>`

o parâmetro `<arquivo>` é o arquivo que contém o código em d+.

## Interpretando a saída

### Léxico

Ao utilizar a análise léxica, o arquivo `log-lexico.txt` será gerado. Esse arquivo possuirá uma estrutura parecida com essa:

```
PR_MAIN            | main
SP_ABREPARENTESES  | (
SP_FECHAPARENTESES | )
PR_WHILE           | while
ID                 | a
OP_IGUAL           | =
LB_BOOL            | true
PR_DO              | do
PR_PRINT           | print
SP_ABREPARENTESES  | (
ID                 | a
SP_FECHAPARENTESES | )
PR_LOOP            | loop
SP_PONTOEVIRGULA   | ;
```

Do lado esquerdo, é o token retornado, e do lado direito, é o lexema referente aquele token.


### Sintático

Ao utilizar a análise sintática, o arquivo `log-sintatico.txt` será gerado. Esse arquivo possuirá uma estrutura parecida com essa:

```
PR_MAIN decl_main OK
SP_ABREPARENTESES decl_main OK
SP_FECHAPARENTESES  decl_main  OK
PR_IF com_selecao OK
ID  var OK
```

Cada linha possui três informações, separadas por um `\t`. A primeira, é o token que foi analisado. A segunda, é o nome da função (regra da gramática) que
gerou o log. E a terceira, é se a análise está certa. Caso ocorra algum erro, Ao invés de `“OK”`, terá uma mensagem, no seguinte formato `“Esperado %s.
Recebido %s”`.
