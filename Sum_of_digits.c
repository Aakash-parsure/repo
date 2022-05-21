#include<stdio.h>

int main()
{
	int i, num,rem=0,sum=0;

	printf("Enter a number : ");
	scanf("%d",&num);

	while(num>0)
	{
		rem=num%10;
		sum=sum+rem;
		num=num/10;
	}
	printf("Sum of the digits is = %d\n",sum);
	return 0;
}
