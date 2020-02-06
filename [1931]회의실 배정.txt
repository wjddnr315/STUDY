#include <stdio.h>
#include <stdlib.h>
#define MAX 100001
int sorted[MAX][2];
void merge(int arr[][2], int left, int mid, int right)
{
	int i, j, k, l;
	i = left;
	j = mid+1;
	k = left;
	while (i <= mid && j <= right)
	{
		if (arr[i][1] <= arr[j][1])
		{
			sorted[k++][1] = arr[i++][1];
			sorted[k++][0] = arr[i++][0];
		}
		else
		{
			sorted[k++][1] = arr[j++][1];
			sorted[k++][0] = arr[j++][0];
		}
	}
	if (i > mid)
	{
		for (l = j; l <= right;l++)
		{
			sorted[k++][1] = arr[l][1];
			sorted[k++][0] = arr[l][0];

		}
	}
	else
	{
		for (l = i; l <= mid;l++)
		{
			sorted[k++][1] = arr[l][1];
			sorted[k++][0] = arr[l][0];

		}
	}
	for (int t = left; t <= right;t++)
	{
		arr[t][1] = sorted[t][1];
		arr[t][0] = sorted[t][0];
	}
	
}
void mergesort(int arr[][2], int left, int right)
{
	int mid;
	if (left <right)
	{
		mid = (right + left) / 2;
		mergesort(arr, left, mid);
		mergesort(arr, mid + 1, right);
		merge(arr, left, mid, right);
	}
	else return;
}
int main(void)
{
	int N, tmp, cnt = 1,tp;
	int arr[MAX][2];

	scanf("%d", &N);
	for (int i = 0; i < N;i++) scanf("%d %d", &arr[i][0], &arr[i][1]);
	mergesort(arr, 0, N - 1);

	tmp = arr[0][1];
	for (int i = 0; i < N-1;i++)
	{
		if (i >= 1 && arr[i - 1][1] == arr[i][1])
		{
			if (arr[i - 1][0] > arr[i][0])
			{
				tp = arr[i - 1][0];
				arr[i - 1][0] = arr[i][0];
				arr[i][0] = tp;
				tp = arr[i - 1][1];
				arr[i - 1][1] = arr[i][1];
				arr[i][1] = tp;
			}
		}
		if (tmp <= arr[i + 1][0])
		{
			tmp = arr[i + 1][1];
			cnt++;
		}
	}
	printf("\n");
	for (int i = 0; i < N;i++) printf("%d %d\n", arr[i][0], arr[i][1]);
	printf("%d", cnt);
	return 0;
}

