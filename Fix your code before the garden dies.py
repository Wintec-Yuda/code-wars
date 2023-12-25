def rain_amount(mm):
    mm = int(mm)
    if (mm < 40):
        return "You need to give your plant " + str(40 - mm) + "mm of water"
    else:
        return "Your plant has had more than enough water for today!"

print(rain_amount(100))
print(rain_amount(40))
print(rain_amount(5))
print(rain_amount(0))