#include <stdio.h>

#define MAX 50

void swap(char*, char*);

int main(void)
{
	char arr[MAX][MAX];
	int number,candycnt=1,max=1;

	scanf("%d", &number);
	getchar();

	for (int i = 0; i < number;i++)
	{
		for (int j = 0; j < number;j++)
		{
			scanf(" %c", &arr[i][j]);
		}
	}
	
	for (int i = 0; i < number;i++)
	{
		for (int j = 0; j < number - 1;j++)
		{
			 swap(&arr[i][j], &arr[i][j + 1]); 
			 for (int i = 0; i < number;i++)
			 {
				 for (int j = 0; j < number - 1;j++)
				 {
					 if (arr[j][i] == arr[j + 1][i])
					 {
						 candycnt++;
						 if (max < candycnt) max = candycnt;
					 }
					 else candycnt = 1;
				 }
				 candycnt = 1;
			 }
			 
			 swap(&arr[i][j], &arr[i][j + 1]);
		}
	}
	for (int j = 0; j < number;j++)
	{
		for (int i = 0; i < number-1;i++)
		{
			swap(&arr[i][j], &arr[i + 1][j]);

			for (int i = 0; i < number;i++)
			{
				for (int j = 0; j < number - 1;j++)
				{
					if (arr[i][j] == arr[i][j + 1])
					{
						candycnt++;
						if (max < candycnt) max = candycnt;
					}
					else candycnt = 1;
				}
				candycnt = 1;
			}
			
			 swap(&arr[i][j], &arr[i + 1][j]);
		}
	}
	printf("%d\n", max);

	return 0;
}
void swap(char *a, char* b)
{
	char temp;
	temp = *a;
	*a = *b;
	*b = temp;
}
