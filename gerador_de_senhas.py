# random: módulo de números aleatórios do Python
# randint(a, b): sorteia um número inteiro entre a e b (inclusive)
# choice(lista): sorteia um elemento de uma lista
# shuffle(lista): embaralha a lista no lugar (altera a própria lista)
from random import randint, choice, shuffle


# Cada caractere tem um código numérico na tabela ASCII.
# chr(número) converte o código no caractere correspondente.
# Ex.: chr(65) -> 'A', chr(97) -> 'a', chr(48) -> '0'

def zero_a_nove():
    # Códigos 48 a 57 são os dígitos '0' a '9'
    return chr(randint(48, 57))


def a_a_z():
    # Códigos 97 a 122 são as letras minúsculas 'a' a 'z'
    return chr(randint(97, 122))


def A_a_Z():
    # Códigos 65 a 90 são as letras maiúsculas 'A' a 'Z'
    return chr(randint(65, 90))


def strange_chars():
    # Os símbolos ficam espalhados em quatro faixas da tabela ASCII,
    # separadas pelos números e pelas letras.
    # Aqui sorteamos um código de cada faixa e guardamos os quatro na lista.
    rand_range = [
        randint(32, 47),    # espaço e símbolos como ! " # $ % & ' ( ) * + , - . /
        randint(58, 64),    # : ; < = > ? @
        randint(91, 96),    # [ \ ] ^ _ `
        randint(123, 126),  # { | } ~
    ]

    # Os comentários abaixo são as mesmas faixas escritas como
    # expressão regular (usada para validar senhas em outros contextos)
    # [\u0020-\u002F\u003A-\u0040\u005B-\u0060\u007B-\u007E]
    # [ -\/:-@[-`{-~]

    # choice sorteia uma das quatro faixas, e chr converte o código em símbolo
    return chr(choice(rand_range))


def create_pass(
        length=12,      # tamanho da senha (padrão: 12 caracteres)
        upper=True,     # incluir letras maiúsculas?
        lower=True,     # incluir letras minúsculas?
        numbers=True,   # incluir números?
        chars=True      # incluir símbolos?
):
    # Lista vazia onde os caracteres serão guardados
    password = []

    # A cada volta, adiciona um caractere de cada tipo ativado.
    # O laço repete 'length' vezes, então a lista passa do tamanho
    # necessário (com os quatro tipos, são 4 por volta).
    for i in range(length):
        if numbers:
            password.append(zero_a_nove())
        if lower:
            password.append(a_a_z())
        if upper:
            password.append(A_a_Z())
        if chars:
            password.append(strange_chars())

    # Corta a lista no tamanho pedido, descartando o excesso
    password = password[:length]

    # Embaralha, para que os tipos não fiquem sempre na mesma ordem
    # (número, minúscula, maiúscula, símbolo, número...)
    shuffle(password)

    # Junta a lista de caracteres em uma única string
    return ''.join(password)


# Só roda quando o arquivo é executado diretamente (python arquivo.py).
# Se outro arquivo importar este módulo, esta parte é ignorada.
if __name__ == '__main__':

    # Teste 1: todos os tipos ativados, 5 senhas de 12 caracteres
    print('VÁLIDAS')
    for i in range(5):
        print(create_pass(
            length=12,
            chars=True,
            upper=True,
            lower=True,
            numbers=True
        ))
    print()  # linha em branco para separar os testes

    # Teste 2: só maiúsculas, números e símbolos
    print('SEM MINÚSCULAS')
    for i in range(5):
        print(create_pass(
            length=12,
            chars=True,
            upper=True,
            lower=False,
            numbers=True
        ))
    print()

    # Teste 3: só maiúsculas e símbolos
    print('SEM MINÚSCULAS E NÚMEROS')
    for i in range(5):
        print(create_pass(
            length=12,
            chars=True,
            upper=True,
            lower=False,
            numbers=False
        ))
    print()

    # Teste 4: só maiúsculas
    print('SEM NÚMEROS CARACTERES E MINÚSCULAS')
    for i in range(5):
        print(create_pass(
            length=12,
            chars=False,
            upper=True,
            lower=False,
            numbers=False
        ))
    print()

    # Teste 5: tamanho pequeno (6), com os parâmetros padrão.
    # Ele é aceito sem erro: o código não valida o tamanho mínimo.
    print('QUANTIDADE INVÁLIDA (6)')
    for i in range(5):
        print(create_pass(
            length=6,
        ))
    print()
