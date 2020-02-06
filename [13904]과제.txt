#include <stdio.h>
#include <stdlib.h>
#define MAX 1001
#define SWAP(x,y){int tmp=x;x=y;y=tmp;}
int compare(const void *first, const void *second)
{
	if (*((int*)second + 1) > *((int*)first + 1))
	{
		return 1;
	}
	else if (*((int*)second + 1) < *((int*)first + 1))
	{
		return -1;
	}
	else
	{
		if (*(int*)second > *(int*)first)
			SWAP(*(int*)second ,*(int*)first);
	}
	return  0;
}
int main(void)
{
	int N, a[MAX][2],res=0,cnt=0;
	int b[MAX] = { 0, };
	scanf("%d", &N);
	for (int i = 0; i < N;i++)
		scanf("%d %d", &a[i][0], &a[i][1]);
	qsort(a, N, sizeof(int) * 2, compare);
	int i = 0;
	for (int i = 0; i < N;i++)
	{
		cnt = a[i][0];
		if (b[cnt] <= 0)
		{
			b[cnt] = a[i][1];
		}
		else
		{
			while (cnt>0)
			{
				if (b[cnt] <= 0)
				{
					b[cnt] = a[i][1];
					break;
				}
				cnt--;
			}
		}
	}
	for (int i = 0; i < 1001;i++)
	{
		res += b[i];
	}
	printf("%d", res);
	return 0;
}