#include <stdio.h>
#include <math.h>

void update(int *a,int *b) {
    int aux = *a + *b;
    *b = abs(*a - *b);
    *a = aux;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}