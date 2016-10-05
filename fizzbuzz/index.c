#include <stdio.h>

void main()
{
  char *fizzed[4] = {NULL, "Fizz", "Buzz", "Fizzbuzz"};
  int i;

  for(i = 1; i <= 100; i++) {
    char *p = fizzed[((i % 5 == 0) << 1) | (i % 3) == 0];
    p ? puts(p) : printf("%d\n", i);
  }
}
