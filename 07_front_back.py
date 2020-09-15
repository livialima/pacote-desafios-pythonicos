"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""
# First Commit
def is_odd(num):
    return num%2

def front_back(a, b):
    #treat a
    a_len = len(a)

    if is_odd(a_len):
        a_len = int(a_len/2) + 1
    else:
        a_len = int(a_len/2)

    a_frente = a[:a_len:]
    a_tras = a[a_len::]

    #treat b
    b_len = len(b)

    if is_odd(b_len):
        b_len = int(b_len/2) + 1
    else:
        b_len = int(b_len/2)

    b_frente = b[:b_len:]
    b_tras = b[b_len::]

    return a_frente + b_frente + a_tras + b_tras


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
