/* #include "header.h" */  

#include <stdio.h>

int main(){

    char ch[] = "_putchar";
    
    int i;

    for (i = 0; i != '\n'; i++){

        putchar(ch[i]);

        printf("\tnext\t");
    }

    putchar('\n');

    return (0);
}