def cek_number(x):
    angka = ''
    for karakter in x:
        if karakter.isdigit():
            angka += karakter
    return int(angka) if angka else 0

def order(sentence):
    # code here
    sentence = sentence.split()
    n = len(sentence)

    for i in range(n):
        for j in range(0, n-i-1):
            if cek_number(sentence[j]) > cek_number(sentence[j+1]):
                sentence[j], sentence[j+1] = sentence[j+1], sentence[j]
    
    return ''.join(sentence)

print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))
print(order(""))
print(order("Thi1sis23aT4est"))
print(order("Fo1rthe2g3ood4ofth5epe6ople"))