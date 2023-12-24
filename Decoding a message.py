def decode(message):
    alphabets = [chr(i+97) for i in range(26)]
    message = message.lower()
    word = ''

    for x in message:
        if (x == ' '):
            word += x
        else:
            i_x = alphabets.index(x)
            word += alphabets[-i_x - 1]
    
    return word


print(decode("sr"))