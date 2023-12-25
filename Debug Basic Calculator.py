def calculate(a, o, b):
    
    if (o == "/" and b == 0):
        return None
    if(o == "+"):
        return a + b
    elif(o == "-"):
        return a - b
    elif(o == "/"):
        return a / b
    elif(o == "*"):
        return a * b
    else:
        return None

print(calculate(-3,"/", 0))
print(calculate(8,"m", 2))
print(calculate(2,"+", 4))
print(calculate(6,"-", 1.5))