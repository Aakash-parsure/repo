#include<stdio.h>

int main()
{
	int i, num;
	long int fact;

	printf("Enter an integer number: ");
	scanf("%d",&num);

	fact=1;
	for(i=num;i>=1;i--)
	{
		fact=fact*i;
	}
	printf("\nFactorial of %d is = %ld\n",fact);
	return 0;
}
