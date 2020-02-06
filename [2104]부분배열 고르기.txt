#include <stdio.h>
#define MAX(a,b) ((a) > (b) ? (a) : (b))
int A[100001];
long long m(int s, int e)
{
	if (e == s) return (long long)A[s] * A[s];
	long long result;
	long long tt;
	int min;
	long long sum;
	int mid = (s + e) / 2;
	result = MAX(m(s, mid), m(mid+1, e));

	int l = mid, r = mid;
	min = A[l];	
	sum = A[l];
	tt = sum * min;

	while (r-l<=e-s)
	{
		int p = l > s ? A[l - 1] : -1; 
		int q = r < e ?  A[r + 1] : -1;
		if ( p < q)
		{
			if (min > q) min = q;
			sum += A[++r];
		}
		else
		{
			if (min > p) min = p;
			sum += A[--l];
			
		}
		tt = sum * min;
		result = MAX(tt, result);
	}
	return result;
}
int main()
{
	int N;
	scanf("%d", &N);
	for (int i = 1; i <= N;i++)
		scanf(" %d", A + i);	
	printf("%lld", m(1, N));
}
