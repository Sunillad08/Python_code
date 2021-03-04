def converter(number):
    number = list(str(number))
    if "e" in number:
        n = number.index("e")
        digits = "".join(number[:n])
        a = "".join(number[n+1:])
        return round(float(digits),6),a
    else:
        return round(float("".join(number)),6) , 0

distance_km = float(input("Enter distance : "))

distance_meter = distance_km / 1000
distance_cm = distance_km / 100000
distance_inches = float(distance_km / 39370.1)
distance_feets = float(distance_km / 3280.84)

digits,exp = converter(distance_cm)
print(str(digits) + " x 10^" + str(exp))

digits,exp = converter(distance_inches)
print(str(digits) + " x 10^" + str(exp))

digits,exp = converter(distance_feets)
print(str(digits) + " x 10^" + str(exp))

digits,exp = converter(distance_meter)
print(str(digits) + " x 10^" + str(exp))