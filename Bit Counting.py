def count_bits(n):
    count = 0
    while n:
        count += n % 2
        n >>= 1
    return count

print(count_bits(0))
print(count_bits(4))
print(count_bits(7))
print(count_bits(9))
print(count_bits(10))
print(count_bits(1234))