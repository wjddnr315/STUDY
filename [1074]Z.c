#include <stdio.h>
int row, col,cnt;
void solve(int r, int c, int div)
{
	if (r > row || c > col) {
		cnt += div * div;
        return;
	}
	if (div == 2){
		for (int i = 0; i < 2;i++){
			for (int j = 0; j < 2;j++){
				if (i + r == row && c + j == col) printf("%d", cnt);
				cnt++;
			}
		}
		return;
	}
	div /= 2;
	for (int i = 0; i < 2;i++)
		for (int j = 0; j < 2; j++)
			 solve(r + i * div, c + j * div, div);
}
int main()
{
	int N;
	scanf("%d %d %d", &N,&row,&col);
	solve(0,0,1<<N);
}
