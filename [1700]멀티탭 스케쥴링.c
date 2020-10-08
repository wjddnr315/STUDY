#include <stdio.h>
int main(void)
{
	int N, K, con[100] = { 0, },seq[100],count=0,max_length=0,idx=-1,f=0;
	scanf("%d %d", &N, &K);
	for (int i = 0; i < K;i++)
	{
		scanf(" %d", &seq[i]);
	}

	int a = 0;
	int i = 0;
	while (a < N)
	{
		for (int b = 0; b < N; b++)
		{
			if (seq[i] == con[b]) f = 1;
		}
		if (f)i++;
		else
		{
			con[a] = seq[i];
			a++;
		}
		f = 0;
	}

	while(i < K)
	{
		for (int q = 0; q < N;q++)
		{
			if (con[q] == seq[i])
			{
				i++;
				q = -1;
			}
		}
		if (!(i < K)) break;
		for (int j = 0; j < N;j++)
		{
			int length = 0;
			for (int k = i; k < K;k++)
			{
				if (con[j] == seq[k])
				{
					length = k;
					break;
				}
			}
			if (length == 0)
			{
				max_length = 101;
				idx = j;
				break;
			}
			else if (max_length < length)
			{
				max_length = length;
				idx = j;
			}
		}
		con[idx] = seq[i++];
		count++;
		max_length = 0;	
	}
	printf("%d", count);
	return 0;
}
