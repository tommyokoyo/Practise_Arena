#include <stdio.h>
#include "reset.h"

int main(){

	n = 10;
	*n = &n;
	printf("The value before calling the function",*n);

	reset(*n);

	printf("the value after calling the function is %d",*n);

	return 0;

}

