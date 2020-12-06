#include <stdio.h>
#define _BUFSIZE 1000000
#define B int main() { unsigned char buf[_BUFSIZE]; unsigned char *p = buf;
#define R ++p;
#define L --p;
#define I ++*p;
#define D --*p;
#define P putchar(*p);
#define G *p = getchar();
#define W while(*p) {
#define E }
