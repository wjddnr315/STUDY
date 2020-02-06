#include <stdio.h>
#define MAX 865
int main(void)
{
	int q, cnt = 0, strike = 0, ball = 0,getstrike[100],getball[100],cntcnt=0;
	char gamech[MAX][4], getnumber[100][4];
	scanf("%d", &q);
	getchar();
	for (int i = 123;i < MAX+123;i++)
	{
		int j = i;
		gamech[i-123][2] = '0' + (j % 10);
		j /= 10;
		gamech[i - 123][1] = '0' + (j % 10);
		j /= 10;
		gamech[i - 123][0] = '0' + (j % 10);
	}
	for (int p = 0;p < q; p++)
	{
		for (int i = 0;i < 4;i++) { scanf("%c", &getnumber[p][i]);}
		scanf("%d%d", &getstrike[p], &getball[p]);
		getchar();
	}
	for (int i = 0;i < MAX;i++)
	{
		if (gamech[i][0] !=gamech[i][1] && gamech[i][1] != gamech[i][2]&& gamech[i][0]!=gamech[i][2]&& gamech[i][0]!='0' && gamech[i][1] != '0' && gamech[i][2] != '0') {

			for (int j = 0; j < q;j++)
			{
				for (int k = 0; k < 3;k++) { if (gamech[i][k] == getnumber[j][k]) { strike++; } }

				if (gamech[i][0] == getnumber[j][1]) { ball++; }
				if (gamech[i][0] == getnumber[j][2]) { ball++; }
				if (gamech[i][1] == getnumber[j][0]) { ball++; }
				if (gamech[i][1] == getnumber[j][2]) { ball++; }
				if (gamech[i][2] == getnumber[j][0]) { ball++; }
				if (gamech[i][2] == getnumber[j][1]) { ball++; }

				if ((getstrike[j] == strike) && (getball[j] == ball)) { cnt++; }
				ball = 0; strike = 0;
			}
			if (cnt == q) { cntcnt++; printf("%c%c%c\n", gamech[i][0], gamech[i][1], gamech[i][2]); }
			cnt = 0;
		}
	}	
	printf("%d", cntcnt);
	return 0;
}
