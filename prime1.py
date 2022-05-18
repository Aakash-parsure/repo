n=int(input("Enter a number: "))
flag = False

if n>1:
    for i in range(2,n):
        if(n%i == 0):
            flag = True
            break


if flag:
    print("{} is not a prime".format(n))
else:
    print("{} is a prime".format(n))
