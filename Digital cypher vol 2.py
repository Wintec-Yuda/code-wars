def decode(code, key):
    alphabets = [chr(i + 97) for i in range(26)]
    key = str(key)
    key = list(key)
    i_key = 0
    encodes = ''

    for x in code:
        x -= int(key[i_key])
        i_key += 1
        if(i_key == len(key)):
            i_key = 0
        encodes += alphabets[x-1]

    return encodes

print(decode([20, 12, 18, 30, 21], 1939))