list = input("Enter a list of numbers separated by spaces: ").split()
list = [int(l) for l in list]
print(list)
print("maximum:",max(list))
print("minimum:",min(list))