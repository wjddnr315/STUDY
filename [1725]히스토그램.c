#include <stdio.h>
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) > (b) ? (b) : (a))
int A[100001];

int m(int s, int e)
{
	if (e == s) return A[s];
	int result;
	int mid = (e + s) / 2;
	result = MAX(m(s, mid), m(mid + 1, e));

	int l = mid, r = mid, h = A[mid];
	
	while (r - l <= e - s)
	{
		int p  =  l > s ? MIN(A[l-1],h) : -1;
		int q  =  r < e ? MIN(A[r+1],h) : -1;
		if (p > q)
		{
			h = p;
			l--;
		}
		else
		{
			h = q;
			r++;
		}
		result = MAX(result, (r-l+1) * h);	
	}
	return result;
}
int main()
{
	int N;
	scanf("%d", &N);
	for (int i = 1; i <= N;i++)
		scanf("%d", A + i);
	printf("%d", m(1, N));
}
