#include<stdio.h>

int main()
{
	int num, rev=0, rem=0, temp=0;
	printf("Enter a number : ");
	scanf("%d",&num);

	temp=num;

	while(temp != 0)
	{
		temp=temp%10;
		rev=rev*10 + rem;
		temp/=10;
	}

	if(rev == num)
		printf("%d is a palindrome number\n",num);
	else
		printf("%d is not a palindrome number\n",num);

	return 0;
}
