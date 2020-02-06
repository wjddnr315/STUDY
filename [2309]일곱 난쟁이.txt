#include <stdio.h>
#include <stdlib.h>

int  main(void)
{
	int arr[9],sum=0,tmp =0;

	for(int n = 0;n < 9;n++)
	{
		scanf("%d", &arr[n]);
	}

	for (int a = 0; a < 9;a++)
	{
		sum += arr[a];
	}

	for (int i = 0; i < 9; i++)
	{
		for (int j = 0; j < 9;j++)
		{
			if (i!=j && (sum - arr[i] - arr[j]) == 100)
			{
				arr[i] = -1;
				arr[j] = -1;
				j = 9;
				i = 9;
				
			}
		}
	}
	for (int i = 0; i < 9; i++)
	{
		for (int j = i; j < 9;j++)
		{
			if (arr[i] > arr[j])
			{
				tmp = arr[i];
				arr[i] = arr[j];
				arr[j] = tmp;
			}
		}
	}
	for (int i = 2; i < 9; i++)
	{
		printf("%d\n", arr[i]);
	}

	return 0;	
}