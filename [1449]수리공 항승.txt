#include <stdio.h>
#define MAX 1001

int main(void)
{
	int N, L, water[MAX], val,cnt=0,temp;
	scanf("%d %d", &N, &L);
	for (int i = 0;i < N;i++)
	{
		scanf("%d", &val);
		water[i] = val;
	}
	for (int i = 0; i < N;i++)
	{
		for (int j = i+1;j < N;j++)
		{
			if (water[i] > water[j])
			{
				temp = water[i];
				water[i] = water[j];
				water[j] = temp;
			}
		}
	}
	for (int i = 0; i < N; i++)
	{
		for (int j = 1; j <N;j++)
		{
			if (water[j] - water[i] + 1 > L)
			{
				cnt++;
				i = j;
				j = i;
			}
		}
	}
	printf("%d",cnt+1);
}