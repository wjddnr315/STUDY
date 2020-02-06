#include <stdio.h>
#include <stdlib.h>

int  main(void)
{
	int	N,K;
	int sum, cmp;
	scanf("%d", &N);
	
	for (int i = 0; i < N; i++)
	{
		sum = i;
		cmp = i;
		while (cmp)
		{
			sum += cmp % 10;
			cmp = cmp / 10;
		}
		if (N == sum)
		{
			K = i;
			break;
		}
		else K = 0;
	}
	printf("%d", K);
	return 0;	
}