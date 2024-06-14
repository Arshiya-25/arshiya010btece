unit=input("is unit fahrenheit or celsius: ")
if unit=='C':
    celsius=float(input("enter temperature in celsius: "))
    fahrenheit=(celsius*9/5)+32
    print("temperature in fahrenheit: ",fahrenheit)
elif unit=='F':
    fahrenheit=float(input("enter temperature in fahrenheit: "))
    celsius=(fahrenheit-32)*5/9
    print("temperature in celsius: ",celsius)
else:
    print("invalid unit")



