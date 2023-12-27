def unique_in_order(sequence):
    result = []
    for i in range(len(sequence)):
        if (sequence[i] not in result) or sequence[i] != sequence[i-1]:
            result.append(sequence[i])
    return result

print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD')  )
print(unique_in_order([1, 2, 2, 3, 3]))
print(unique_in_order((1, 2, 2, 3, 3)) )