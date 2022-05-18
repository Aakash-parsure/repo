"""def checkPrime(a):
    if a>1:
        for j in range(2,int(a/2)):
            if(a%j)==0:
                print(a, "is not a prime number")
                break
            else:
                print(a, "is a prime number")
                break
                
    else:
        print(a, "is not a prime number")

a=int(input("Enter a number "))
checkPrime(a)
"""

lower=int(input("Enter the lower limit: "))
upper=int(input("Enter the upper limit: "))

for n in range(lower,upper+1):
    if n>1:
        for i in range(2,n):
            if(n%i == 0):
                break
        else:
            print(n)

