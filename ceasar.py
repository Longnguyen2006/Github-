def caesar_cipher(message, mode, key):
    
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message = message.upper()
    translated = ''
    
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            if mode.upper() == 'ENCRYPT':
                num = (num + key) % 26
            elif mode.upper() == 'DECRYPT':
                num = (num - key) % 26
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol

    return translated

message = 'SEE YOU AGAIN'
cipher = caesar_cipher(message, 'ENCRYPT', 13)
print('Plain text:  ' + message)
print('Cipher text: ' + cipher)