def encode(message, key):
    alphabets = [chr(i + 97) for i in range(26)]
    key = str(key)
    key = list(key)
    i_key = 0
    encodes = []

    for x in message:
        for i in range(26):
            if alphabets[i] == x:
                i_alphabet = alphabets.index(x)
                i_alphabet += int(key[i_key])
                i_key += 1
                encodes.append(i_alphabet + 1)
                if(i_key == len(key)):
                    i_key = 0

    return encodes


print(encode("scout", 1939))