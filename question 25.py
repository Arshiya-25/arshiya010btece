file1 = input("Enter the path of the source file: ")
file2 = input("Enter the path of the destination file: ")

with open(file1, 'r') as source:
    with open(file2, 'w') as destination:
        destination.write(source.read())