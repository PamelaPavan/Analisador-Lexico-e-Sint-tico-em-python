# Alunos: João Paulo Matos Mendes e Pâmela Aliny Cleto Pavan
# Disciplina: Linguagens Formais e Autômatos
# Professor: Faimison Rodrigues Porto
#
# Implementação de Analisadores Léxico e Sintático (referente à questão 5 da lista 3)

# TOKENS
DIGITOS = "0123456789";
VARIAVEIS = "abcdefghijklmnopqrstuvwxyz0123456789";
VAZIOS = " \n\r\t";
SEPARADORES = ",;";
OPERADORES = "+-*/";
ABRE_PARENTESES = "(";
FECHA_PARENTESES = ")";
ABRE_COLCHETES = "[";
FECHA_COLCHETES = "]";
ABRE_CHAVES = "{";
FECHA_CHAVES = "}";

# NOME DO ARQUIVO
NOME_DEFAULT_ARQUIVO_ENTRADA = "entrada.txt";

# VARIÁVEIS
lista_tokens = [];
tudo_certo = True;

# ANALISADOR LÉXICO
def verificacao_digito(texto_arquivo):
  global lista_tokens;
  global tudo_certo;

  # Verifica se o caractere atual do arquivo é um dígito
  if texto_arquivo[0] in DIGITOS:
    # Verifica se é o último caractere do arquivo
    if len(texto_arquivo) > 1:
      verificacao_digito(texto_arquivo[1:]);
    else:
      print("<NUMERO>");
      lista_tokens.append("<NUMERO>");
      verificacao_inicial(texto_arquivo[1:]);
  # Verifica se é o caractere atual do arquivo existe na lista de caracteres válidos
  elif texto_arquivo[0] in OPERADORES + ABRE_PARENTESES + FECHA_PARENTESES + ABRE_COLCHETES + FECHA_COLCHETES + ABRE_CHAVES + FECHA_CHAVES + VAZIOS + SEPARADORES:
    print("<NUMERO>");
    lista_tokens.append("<NUMERO>");
    verificacao_inicial(texto_arquivo[:]);
  # Se não, informa um erro léxico
  else:
    tudo_certo = False;
    print("Erro léxico! Caractere encontrado: '" + texto_arquivo[0] + "'");
    print("Era(m) esperado(s): " + DIGITOS + "'");

def verificacao_variavel(texto_arquivo):
  global lista_tokens;
  global tudo_certo;

  # Verifica se o caractere atual do arquivo é uma variável
  if texto_arquivo[0] in VARIAVEIS:
    # Verifica se é o último caractere do arquivo
    if len(texto_arquivo) > 0:
      verificacao_variavel(texto_arquivo[1:]);
    else:
      print("<VARIAVEL>");
      lista_tokens.append("<VARIAVEL>");
      verificacao_inicial(texto_arquivo[1:]);
  # Verifica se é o caractere atual do arquivo existe na lista de caracteres válidos
  elif texto_arquivo[0] in OPERADORES + ABRE_PARENTESES + FECHA_PARENTESES + ABRE_COLCHETES + FECHA_COLCHETES + ABRE_CHAVES + FECHA_CHAVES + VAZIOS + SEPARADORES:
    print("<VARIAVEL>");
    lista_tokens.append("<VARIAVEL>");
    verificacao_inicial(texto_arquivo[:]);
  # Se não, informa um erro léxico
  else:
    tudo_certo = False;
    print("Erro léxico! Caractere encontrado: '" + texto_arquivo[0] + "'");
    print("Era(m) esperado(s): " + VARIAVEIS + "'");

def verificacao_operador(texto_arquivo):
  global lista_tokens;
  global tudo_certo;

  # Verifica se o caractere atual do arquivo é um operador
  if texto_arquivo[0] in OPERADORES:
    print("<OPERADOR>");
    lista_tokens.append("<OPERADOR>");
    verificacao_inicial(texto_arquivo[1:]);
  # Se não, informa um erro léxico
  else:
    tudo_certo = False;
    print("Erro léxico! Caractere encontrado: '" + texto_arquivo[0] + "'");
    print("Era(m) esperado(s): " + OPERADORES + "'");

def verificacao_parenteses(texto_arquivo):
  global lista_tokens;
  global tudo_certo;

  # Verifica se o caractere atual do arquivo é um abre parênteses
  if texto_arquivo[0] in (ABRE_PARENTESES):
    print("<ABRE_PARENTESES>");
    lista_tokens.append("<ABRE_PARENTESES>");
    verificacao_inicial(texto_arquivo[1:]);
  # Verifica se o caractere atual do arquivo é um fecha parênteses
  elif texto_arquivo[0] in (FECHA_PARENTESES):
    print("<FECHA_PARENTESES>");
    lista_tokens.append("<FECHA_PARENTESES>");
    verificacao_inicial(texto_arquivo[1:]);
  # Se não, informa um erro léxico
  else:
    tudo_certo = False;
    print("Erro léxico! Caractere encontrado: '" + texto_arquivo[0] + "'");
    print("Era(m) esperado(s): '" + ABRE_PARENTESES + FECHA_PARENTESES + "'");

def verificacao_colchetes(texto_arquivo):
  global lista_tokens;
  global tudo_certo;

  # Verifica se o caractere atual do arquivo é um abre colchetes
  if texto_arquivo[0] in (ABRE_COLCHETES):
    print("<ABRE_COLCHETES>");
    lista_tokens.append("<ABRE_COLCHETES>");
    verificacao_inicial(texto_arquivo[1:]);
  # Verifica se o caractere atual do arquivo é um abre colchetes
  elif texto_arquivo[0] in (FECHA_COLCHETES):
    print("<FECHA_COLCHETES>");
    lista_tokens.append("<FECHA_COLCHETES>");
    verificacao_inicial(texto_arquivo[1:]);
  # Se não, informa um erro léxico
  else:
    tudo_certo = False;
    print("Erro léxico! Caractere encontrado: '" + texto_arquivo[0] + "'");
    print("Era(m) esperado(s): " + ABRE_COLCHETES + FECHA_COLCHETES + "'");

def verificacao_chaves(texto_arquivo):
  global lista_tokens;
  global tudo_certo;

  # Verifica se o caractere atual do arquivo é um abre chaves
  if texto_arquivo[0] in (ABRE_CHAVES):
    print("<ABRE_CHAVES>");
    lista_tokens.append("<ABRE_CHAVES>");
    verificacao_inicial(texto_arquivo[1:]);
  # Verifica se o caractere atual do arquivo é um abre chaves
  elif texto_arquivo[0] in FECHA_CHAVES:
    print("<FECHA_CHAVES>");
    lista_tokens.append("<FECHA_CHAVES>");
    verificacao_inicial(texto_arquivo[1:]);
  # Se não, informa um erro léxico
  else:
    tudo_certo = False;
    print("Erro léxico! Caractere encontrado: '" + texto_arquivo[0] + "'");
    print("Era(m) esperado(s): " + ABRE_CHAVES + FECHA_CHAVES + "'");

def verificacao_eof():
  global lista_tokens;
  global tudo_certo;

  # Informa que o arquivo foi lido até o fim
  print("<EOF>\n");
  print("Análisa léxica realizada com sucesso no arquivo '" + NOME_DEFAULT_ARQUIVO_ENTRADA + "'");

def verificacao_inicial(texto_arquivo):
  global lista_tokens;
  global tudo_certo;

  # Verifica se existem caracteres a serem lidos
  if len(texto_arquivo) > 0:
    # Verifica o caractere atual do arquivo é vazio
    if texto_arquivo[0] in VAZIOS:
      verificacao_inicial(texto_arquivo[1:]);
    # Verifica o caractere atual do arquivo é um separador
    elif texto_arquivo[0] in SEPARADORES:
      lista_tokens.append("<SEPARADOR>");
      print("\n<SEPARADOR>\n");
      verificacao_inicial(texto_arquivo[1:]);
    # Verifica o caractere atual do arquivo é um digito
    elif texto_arquivo[0] in DIGITOS:
      verificacao_digito(texto_arquivo);
    # Verifica o caractere atual do arquivo é uma variável
    elif texto_arquivo[0] in VARIAVEIS:
      verificacao_variavel(texto_arquivo);
    # Verifica o caractere atual do arquivo é um operador
    elif texto_arquivo[0] in OPERADORES:
      verificacao_operador(texto_arquivo);
    # Verifica o caractere atual do arquivo é um abre ou fecha parênteses
    elif texto_arquivo[0] in ABRE_PARENTESES + FECHA_PARENTESES:
      verificacao_parenteses(texto_arquivo);
    # Verifica o caractere atual do arquivo é um abre ou fecha colchetes
    elif texto_arquivo[0] in ABRE_COLCHETES + FECHA_COLCHETES:
      verificacao_colchetes(texto_arquivo);
    # Verifica o caractere atual do arquivo é um abre ou fecha chaves
    elif texto_arquivo[0] in ABRE_CHAVES + FECHA_CHAVES:
      verificacao_chaves(texto_arquivo);
    
    # Verifica se é o caractere atual do arquivo existe na lista de caracteres válidos
    elif texto_arquivo[0] in VARIAVEIS + OPERADORES + ABRE_PARENTESES + FECHA_PARENTESES + ABRE_COLCHETES + FECHA_COLCHETES + ABRE_CHAVES + FECHA_CHAVES + VAZIOS + SEPARADORES:
      verificacao_eof();
    # Se não, informa um erro léxico
    else:
      tudo_certo = False;
      print("Erro léxico! Caractere encontrado: '" + texto_arquivo[0] + "'");
      print("Era(m) esperado(s): '" + VARIAVEIS + OPERADORES + ABRE_PARENTESES + FECHA_PARENTESES + ABRE_COLCHETES + FECHA_COLCHETES + ABRE_CHAVES + FECHA_CHAVES + "'");
  else:
    verificacao_eof();

# FUNÇÕES AUXILIARES
def reconhece(token):
  global lista_tokens;
  global tudo_certo;

  # Verifica se o token atual é o esperado
  if len(lista_tokens) > 0 and lista_tokens[0] == token:
    del lista_tokens[0];
    return;
  elif tudo_certo:
    print("Erro sintático! Token encontrado: " + ("<>" if len(lista_tokens) == 0 else lista_tokens[0]));
    print("Era(m) esperado(s): " + token);
    tudo_certo = False;

# ANALISADOR SINTÁTICO
# Parte da gramática que complementa S2
def C():
  global lista_tokens;
  global tudo_certo;

  if len(lista_tokens) > 0 and lista_tokens[0] == "<OPERADOR>":
    reconhece("<OPERADOR>"); S2(); C();
  else:
    return;

# Parte da gramática que complementa S1
def B():
  global lista_tokens;
  global tudo_certo;

  if len(lista_tokens) > 0 and lista_tokens[0] == "<OPERADOR>":
    reconhece("<OPERADOR>"); S1(); B();
  else:
    return;

# Parte da gramática que complementa S
def A():
  global lista_tokens;
  global tudo_certo;

  if len(lista_tokens) > 0 and lista_tokens[0] == "<OPERADOR>":
    reconhece("<OPERADOR>"); S(); A();
  else:
    return;

# Parte da gramática inicial, onde pode variáveis, números e parênteses
def S2():
  global lista_tokens;
  global tudo_certo;

  if len(lista_tokens) > 0 and lista_tokens[0] == "<VARIAVEL>":
    reconhece("<VARIAVEL>"); C();
  elif len(lista_tokens) > 0 and lista_tokens[0] == "<NUMERO>":
    reconhece("<NUMERO>"); C();
  elif len(lista_tokens) > 0 and lista_tokens[0] == "<ABRE_PARENTESES>":
    reconhece("<ABRE_PARENTESES>"); S2(); reconhece("<FECHA_PARENTESES>"); C();
  elif tudo_certo:
    print("Erro sintático! Token encontrado: " + ("<>" if len(lista_tokens) == 0 else lista_tokens[0]));
    print("Era(m) esperado(s): <VARIAVEL> <NUMERO> <ABRE_PARENTESES>");
    tudo_certo = False;

# Parte da gramática inicial, onde pode variáveis, números, parênteses e colchetes
def S1():
  global lista_tokens;
  global tudo_certo;

  if len(lista_tokens) > 0 and lista_tokens[0] == "<VARIAVEL>":
    reconhece("<VARIAVEL>"); B();
  elif len(lista_tokens) > 0 and lista_tokens[0] == "<NUMERO>":
    reconhece("<NUMERO>"); B();
  elif len(lista_tokens) > 0 and lista_tokens[0] == "<ABRE_PARENTESES>":
    reconhece("<ABRE_PARENTESES>"); S2(); reconhece("<FECHA_PARENTESES>"); B();
  elif len(lista_tokens) > 0 and lista_tokens[0] == "<ABRE_COLCHETES>":
    reconhece("<ABRE_COLCHETES>"); S1(); reconhece("<FECHA_COLCHETES>"); B();
  elif tudo_certo:
    print("Erro sintático! Token encontrado: " + ("<>" if len(lista_tokens) == 0 else lista_tokens[0]));
    print("Era(m) esperado(s): <VARIAVEL> <NUMERO> <ABRE_PARENTESES> <ABRE_COLCHETES>");
    tudo_certo = False;

# Parte da gramática inicial, onde pode variáveis, números, parênteses, colchetes e chaves
def S():
  global lista_tokens;
  global tudo_certo;

  if len(lista_tokens) > 0 and lista_tokens[0] == "<VARIAVEL>":
    reconhece("<VARIAVEL>"); A();
  elif len(lista_tokens) > 0 and lista_tokens[0] == "<NUMERO>":
    reconhece("<NUMERO>"); A();
  elif len(lista_tokens) > 0 and lista_tokens[0] == "<ABRE_PARENTESES>":
    reconhece("<ABRE_PARENTESES>"); S2(); reconhece("<FECHA_PARENTESES>"); A();
  elif len(lista_tokens) > 0 and lista_tokens[0] == "<ABRE_COLCHETES>":
    reconhece("<ABRE_COLCHETES>"); S1(); reconhece("<FECHA_COLCHETES>"); A();
  elif len(lista_tokens) > 0 and lista_tokens[0] == "<ABRE_CHAVES>":
    reconhece("<ABRE_CHAVES>"); S(); reconhece("<FECHA_CHAVES>"); A();
  elif tudo_certo:
    print("Erro sintático! Token encontrado: " + ("<>" if len(lista_tokens) == 0 else lista_tokens[0]));
    print("Era(m) esperado(s): <VARIAVEL> <NUMERO> <ABRE_PARENTESES> <ABRE_COLCHETES> <ABRE_CHAVES>");
    tudo_certo = False;

# Função principal
def main():
  global lista_tokens;
  global tudo_certo;

  # Abertura e leitura de arquivo de texto (.txt)
  with open(NOME_DEFAULT_ARQUIVO_ENTRADA, "r", encoding="utf-8") as arquivo_entrada:
    texto_arquivo = arquivo_entrada.read();

  # Realiza a análise léxica
  verificacao_inicial(texto_arquivo);

  # Verifica se ocorreu tudo bem na análise léxica. Se sim, realiza a análise sintática
  if tudo_certo:
    S();
  # Verifica se ocorreu tudo bem na análise sintática. Se sim, informa que o código está correto
  if tudo_certo:
    print("Análisa sintática realizada com sucesso no arquivo '" + NOME_DEFAULT_ARQUIVO_ENTRADA + "'");

main();
