str = input("Enter a string: ")
prefix = input("Enter a prefix to check: ")
suffix = input("Enter a suffix to check: ")

pre = str.startswith(prefix)
suf= str.endswith(suffix)

print("Starts with prefix:", pre)
print("Ends with suffix:", suf)