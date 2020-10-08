#include <stdio.h>
#define MAX 10001

int main(void)
{
	int N, K, max = 0, min = MAX, res = 0,tmp,c,m;
	int x[MAX];
	scanf("%d %d", &N, &K);
	for (int i = 0; i < N;i++)
	{
		scanf(" %d", &x[i]);
	}
	for (int i = 0; i < N-1;i++)
	{
		for (int j = i+1; j < N;j++)
		{
			if (x[i] < x[j])
			{
				tmp = x[i];
				x[i] = x[j];
				x[j] = tmp;
			}
		}
	}
	for (int i = 0; i < N - 1; i++)
		x[i] = x[i] - x[i + 1];
	for (int i = 0; i < K - 1;i++)
	{
		m=x[0];
		c = 0;
		for (int j = 1; j < N - 1;j++)
		{
			if (m < x[j])
			{
				m = x[j];
				c = j;
			}
		}
		x[c] = 0;
	}
	for(int i = 0; i < N-1;i++)
		res += x[i];
	printf("%d", res);
	return 0;
}
