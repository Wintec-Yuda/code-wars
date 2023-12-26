def to_camel_case(text):
    result = ''
    i = 0
    while i < len(text):
        if not text[i].isalpha():
            i += 1
            result += text[i].upper()
        else:
            result += text[i]
        i += 1
    return result

print(to_camel_case(""))
print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-Stealth-Warrior"))
print(to_camel_case("A-B-C"))