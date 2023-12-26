def get_sum(a,b):
    #good luck!
    result = 0
    distance = abs(a-b)
    start = a
    end = b

    if a == b:
        return a

    if b < a:
        start = b
        end = a
    for i in range(start, end+1):
        result += i

    return result

print(get_sum(0,1))
print(get_sum(0,-1))