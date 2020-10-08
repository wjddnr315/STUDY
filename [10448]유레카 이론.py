#include <stdio.h>
#include <math.h>
#define MAX 45
int triangle[MAX];
int ureka(int a);

int main(void)
{
	int testcase,num;

	int temp = 0;

	scanf("%d", &testcase);
	getchar();

	for (int i = 1;i<MAX;i++)
	{
		temp += i;
		triangle[i] = temp;
	}
	for (int i = 0; i < testcase;i++)
	{
		scanf("%d", &num);
		printf("%d\n",ureka(num));
	}
	return 0;
}

int  ureka(int a)
{
	int st = 0;
	for (int i = 1;i < 45;i++)
	{
		for (int j = 1;j < 45;j++)
		{
			for (int k = 1;k < 45;k++)
			{
				if (triangle[i] + triangle[j] + triangle[k] == a)
				{
					st = 1;
					return st;
				}
				else st = 0;

			}
		}
	}
	return st;
}
