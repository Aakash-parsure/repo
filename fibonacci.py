num=int(input("How many terms user wants to print : "))
n1=0
n2=1
count=0

if num<=0:
    print("Please eneter a valid number, the givwn number is not valid\n")

elif num==1:
    print("The Fibonacci sequence of the numbers up to", num)
    print(n1)

else:
    print("The fibonacci sequence of the numbers is ")
    while(count<num):
        print(n1)
        nth = n1 + n2  
        n1 = n2
        n2 = nth  
        count += 1 
