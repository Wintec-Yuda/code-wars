def get_count(sentence):
    count = 0
    for x in sentence:
        if x in 'aiueo':
            count += 1
    if sentence == '':
        return count, f"Incorrect answer for empty string"
    else:
        return count,  f"Incorrect answer for \"{sentence}\""

print(get_count("y"))
print(get_count("bcdfghjklmnpqrstvwxz y"))
print(get_count(""))
print(get_count("abracadabra"))