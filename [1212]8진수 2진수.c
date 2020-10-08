#include <stdio.h>
#include <math.h>
#define MAX 333335
int main(void)
{
	char arr[MAX];

	scanf("%s", arr);
	getchar();

	for (int i = 0;arr[i] != '\0';i++)
	{
		if (i) 
		{
			switch (arr[i])
			{
			case '0': printf("000"); break;
			case '1': printf("001"); break;
			case '2': printf("010"); break;
			case '3': printf("011"); break;
			case '4': printf("100"); break;
			case '5': printf("101"); break;
			case '6': printf("110"); break;
			case '7': printf("111"); break;

			}
		}
		else
		{
			if (arr[i] == '0')printf("0");
			else
			{
				switch (arr[i])
				{
				case '1': printf("1"); break;
				case '2': printf("10"); break;
				case '3': printf("11"); break;
				case '4': printf("100"); break;
				case '5': printf("101"); break;
				case '6': printf("110"); break;
				case '7': printf("111"); break;

				}
			}
		}

	}

	return 0;
}
