#include <stdio.h>
int main(){
    int v[10] = {1,2,3,4,5,6,7,8,9,10};
    int *p;
    p = v;
    printf("p = %p\n", p);
    printf("*p = %d", *p);
    printf("\np[0] = %d", p[0]);
}
