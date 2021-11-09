from cipher_ql2398 import cipher_ql2398
import pytest
def cipher(text, shift, encrypt=True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    assert not isinstance(shift, str), "Shift parameter should not be a string"
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

def test_cipher_1():
    example = 'single'
    expected = 'ukping'
    actual = cipher_ql2398.cipher(example,2)
    assert actual == expected

