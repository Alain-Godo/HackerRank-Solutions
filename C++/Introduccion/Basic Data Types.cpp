#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int a; long int b; char c; float d; double e;
    cin >> a >> b >> c >> d >> e;
    printf("%d\n",a);
    printf("%ld\n",b);
    printf("%c\n",c);
    printf("%.3f\n",d);
    printf("%.9lf\n",e);
    return 0;
}