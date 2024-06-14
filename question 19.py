import string
str1 = input("Enter a string: ")
str2 = str1.translate(str.maketrans('', '', string.punctuation))
print("String without punctuation:", str2)