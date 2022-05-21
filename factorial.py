n=int(input("Enter a number : "))
fact=1

if(n<0):
    print("Factorial dosen't exist.\n")
elif(n==0 or n==1):
    print("Factorial is 1.\n");
else:
    for i in range(1,n+1):
        fact=fact*i;
    print("Factorial of {} is {}.\n".format(n,fact))
