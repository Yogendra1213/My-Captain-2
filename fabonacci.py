no=int(input("Enter no, of terms for the Fabonacci series. Use 0 for an Infinite Fabonacci seies:"))
n1,n2,=0,1
count=0
if no<0:
    print("Enter a positive Number.")
elif no==1:
    print("Your fabonaci series is:",end='\n')
    print(n1+n2)
elif no>1:
    print("Fabonacci series!!")
    while count<no:
        print(n1)
        fab=n1+n2
        n1=n2
        n2=fab
        count +=1
elif no==0:
    print("Fabonacci series!!")
    while True:
        print(n1)
        fab=n1+n2
        n1=n2
        n2=fab
else:
    print("Enter a positive value!!!")
        
