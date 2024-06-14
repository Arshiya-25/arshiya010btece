file=open("C:\\Users\\Yogendra Singh\\Desktop\\demo1.txt","w")
string=input("enter: ")
file.write(string)
file.close()

#OR

'''with open("C:\\Users\\Yogendra Singh\\Desktop\\demo1.txt","w") as file:
    string=input("enter: ")
    file.write(string)'''