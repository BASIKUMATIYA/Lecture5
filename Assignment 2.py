def to_liters(gallons):
    return gallons * 3.78541


while True:
    g = float(input("Gallons: "))
    if g < 0:
        break
    print(to_liters(g))