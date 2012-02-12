#include <stdio.h>
#include <stdlib.h>

long gcd(long x, long y) {
  long t = 0;
  while (y != 0) {
    t = y;
    y = x % y;
    x = t;
  }
  return x;
}

typedef struct { long w; long c; } item;

int main(int argc, char** argv) {
  /* Variable declarations */
  int n = 0;
  int capacity = 50;
  long weight, cost, target, g, i, j, best, c;
  long * table;
  item * items;
  item x;
  FILE *file = fopen(argv[1], "r");
  char* line = malloc(sizeof(char)*255);

  /* Ensure proper input file */
  if ((argc < 1) || (file == NULL)) {
    printf("usage: ./usrbincrash <in>\n");
    free(line);
    exit(1);
  }

  items = malloc(capacity*sizeof(item));
  if (items == NULL) exit(1);
  /* Load the file, ignoring SKU, into struct */
  fscanf(file, "%ld", &target);
  while (fscanf(file, "%s%ld%ld", line, &weight, &cost) == 3) {
    if (n == capacity) {
      capacity *= 2;
      items = realloc(items, capacity*sizeof(item));
      if (items == NULL)
        exit(1);
    }
    x.c = cost;
    x.w = weight;
    items[n] = x;
    n++;
  }
  free(line);
  fclose(file);

  /* Reduce all weights by the GCD */
  g = gcd(target, items[0].w);
  for (i = 1; i < n; i++)
    g = gcd(g, items[i].w);
  if (g > 1) {
    for (i = 0; i < n; i++ ) {
      items[i].w /= g;
    }
    target /= g;
  }

  /* Dynamic Programming Algorithm */
  best = -1;
  table = malloc(sizeof(long) * target);
  for (i = 0; i < target; i++) {
    best = -1;
    for (j = 0; j < n; j++){
      c = items[j].c;
      if (items[j].w <= i)
        c += table[i - items[j].w];
      if ((c < best) || (best == -1))
        best = c;
    } 
    table[i] = best;
  }
  printf("%ld\n", table[target-1]);
  free(items);
  return 0;
}
