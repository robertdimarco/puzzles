#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
  const long long *p1 = a;
  const long long *p2 = b;
  return (((*p1)) - ((*p2)));
}

int main(int argc, char** argv) {
  if (argc < 2) {
    printf("usage: ./recycle-numbers <file.in>\n");
    exit(1);
  }

  int T, j, row;
  long long A, B, i, temp, num_pairs;
  FILE* file = fopen(argv[1], "r");

  fscanf(file, "%d", &T);
  row = 0;
  while (fscanf(file, "%lld %lld", &A, &B) == 2) {
    row++;

    int num_pairs = 0, power = 1, temp = A;
    while (temp >= 10) {
        power *= 10;
        temp /= 10;
    }

    for (i = A; i <= B; i++) {
      temp = i;
      while (1) {
        temp = ((temp % 10) * (power)) + (temp / 10);
        if (temp == i) {
          break;
        } else if ((temp > i) && (temp >= A) && (temp <= B)) {
          num_pairs++;
        }
      }
    }
    printf("Case #%d: %d\n", row, num_pairs);
  }
  fclose(file);
}
