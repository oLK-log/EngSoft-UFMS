#include <stdio.h>

int main(void){
    char s[] = "Dvmuvsb", *p;

    for(p = s; *p; p++){
        --*p;
    }
    printf("%s\n", s);

    return 0;
}
