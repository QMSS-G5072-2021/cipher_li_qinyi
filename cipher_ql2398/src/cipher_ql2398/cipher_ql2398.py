def cipher(text, shift, encrypt=True):
    '''The function takes text, and substitutes each letter with the xth letter next to it. Shift is the x that you can adjust.
    Input: the text you want to encrypt and the number of shift you want to take.
    Output: the encrypted text
    Example: input = 'single' shift = 2 output='upking'
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
