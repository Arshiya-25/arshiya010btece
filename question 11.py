n=int(input("enter the no. of terms: "))
t1=0
t2=1
print("first ",n," terms of fibonnaci series are:")
for i in range(1,n+1):
    print(t1)
    nexterm=t1+t2
    t1=t2
    t2=nexterm
