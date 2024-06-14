num = input("Enter a number: ")
sum = sum(int(digit) for digit in num if digit.isdigit())
print("The sum of the digits of the given number is:", sum)