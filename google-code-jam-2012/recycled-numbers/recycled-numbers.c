#include <math.h>
#include <stdio.h>
#include <stdlib.h>

long long shift(long long n, int length) {
  int first = floor(n / pow(10, floor(log10(n))));
  int last = n % 10;
  long long next = ((n - last) / 10) + (last * pow(10, length - 1));
  return next;
}

int get_length(int n) {
  int len = 0;
  while (n > 0) {
    len++;
    n /= 10;
  }
  return len;
}

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

    num_pairs = 0;
    int length = get_length(A);
    long* permutes = (long*)malloc(sizeof(long*) * length);
    for (i = A; i <= B; i++) {
      temp = i;
      for (j = 1; j < length; j++) {
        temp = shift(temp, length);
        permutes[j-1] = temp;
      }

      qsort(permutes, length-1, sizeof(long), compare);

      for (j = 1; j < length; j++) {
        if ((j > 1) && (permutes[j-1] == permutes[j-2])) continue;
        temp = permutes[j-1];

        if ((temp > i) && (temp >= A) && (temp <= B)) {
          num_pairs++;
        }
      }
    }
    printf("Case #%d: %lld\n", row, num_pairs);
  }
  fclose(file);
}
