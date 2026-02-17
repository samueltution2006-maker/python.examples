#include <stdio.h>

int main() {
    int a=10;
    char b='1';
    float c=10.5;

    print("%d", a);
    print("%c", b);
    print("%f", c);


    print("%d %c %f", a, b, c);
}