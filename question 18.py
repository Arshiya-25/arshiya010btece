str1 = input("Enter the string 1: ").lower()
str2 = input("Enter the string 2: ").lower()


str1 = "".join(char for char in str1 if char.isalnum())
str2 = "".join(char for char in str2 if char.isalnum())


if sorted(str1) == sorted(str2):
    print("The strings are anagrams of each other.")
else:
    print("The strings are not anagrams of each other.")