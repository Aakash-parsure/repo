#include<stdio.h>

int main()
{
	int n,m=0,i,flag=0;
	printf("Enter the number : ");
	scanf("%d",&n);
	if(n==0 || n==1)
	{
		printf("Number is not a prime\n");
		return 0;
	}
	m=n/2;
	for(i=2;i<m;i++)
	{
		if(n%i==0)
		{
		printf("Number is not a prime\n");
		flag=1;
		break;
		}
	}
	if(flag==0)
	{
		printf("Number is a prime\n");
		return 0;


	}
}
