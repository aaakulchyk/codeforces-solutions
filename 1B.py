import math
import re


def rc_to_alphanum(row_number, column_number):
    """Translate R<row_number>C<column_number> to <column><row> form."""
    len_alphabet = ord('Z') - ord('A') + 1
    assert len_alphabet == 26, 'Wrong length of alphabet'
    column = ''
    num_letters = math.ceil(math.log(column_number, len_alphabet))
    position_max = pow(len_alphabet, num_letters)   # Letters Z encode column num 26 ** count.
    
    # Iteratively decrease position maximum to go to the next letter.
    for i in range(1, num_letters+1):
        position_max //= len_alphabet
        letter_code = column_number // position_max
        column_number -= letter_code * position_max
        column += chr(ord('A') - 1 + letter_code)

    return f'{column}{row_number}'
    


def alphanum_to_rc(row, column):
    """Translate <column><row> to R<row_number>C<column_number> form."""
    len_alphabet = ord('Z') - ord('A') + 1
    assert len_alphabet == 26, 'Wrong length of alphabet'
    column_number = 0
    for i, letter in enumerate(reversed(column)):
        column_number += (ord(letter) - ord('A') + 1) * pow(len_alphabet, i)
    return f'R{row}C{column_number}'


rc_regex = re.compile(r'R\d+C\d+')
n = int(input())
for i in range(n):
    in_str = input()
    if re.match(rc_regex, in_str):
        r, c = [int(i) for i in re.split(r'[RC]', in_str) if i != '']
        print(rc_to_alphanum(r, c))
    else:
        r = re.search(r'\d+', in_str).group(0)
        c = re.search(r'[A-Z]+', in_str).group(0)
        print(alphanum_to_rc(r, c))
