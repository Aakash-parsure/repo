#include<stdio.h>
#include<math.h>

int isPerfectSquare(int number)
{
	int ivar;
	float fvar;

	fvar=sqrt((double)number);
	ivar=fvar;

	if(ivar==fvar)
		return 1;
	else
		return 0;
}

int main()
{
	int num;
	printf("Enter an integer : ");
	scanf("%d",&num);

	if(isPerfectSquare(num))
		printf("%d is a perfect square.\n",num);
	else
		printf("%d is not a perfect square.\n",num);

	return 0;
}
