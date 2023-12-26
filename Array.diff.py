def array_diff(a, b):
    result = []
    for x in a:
        if x not in b:
            result.append(x)

    return result

print(array_diff([1,2], [1]))
print(array_diff([1,2,2], [1]))
print(array_diff([1,2,2], [2]))
print(array_diff([1,2,2], []))
print(array_diff([], [1,2]))
print(array_diff([1,2,3], [1, 2]))