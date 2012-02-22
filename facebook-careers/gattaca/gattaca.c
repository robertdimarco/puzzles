#include <stdio.h>
#include <stdlib.h>

typedef struct { long start; long stop; long score; } gene;

/* Adapted from http://www.algolist.net/Algorithms/Sorting/Quicksort */
void quickSort(gene arr[], int left, int right) {
  int i = left, j = right;
  gene tmp;
  gene pivot = arr[(left + right) / 2];

  /* Partition */
  while (i <= j) {
    while (arr[i].start < pivot.start)
      i++;
    while (arr[j].start > pivot.start)
      j--;
    if (i <= j) {
      tmp = arr[i];
      arr[i] = arr[j];
      arr[j] = tmp;
      i++;
      j--;
    }
  };

  /* Recursion */
  if (left < j)
    quickSort(arr, left, j);
  if (i < right)
    quickSort(arr, i, right);
}

int main(int argc, char** argv) {
  /* Variable declarations */
  long i, j = 0, n, length;
  gene x;
  gene * genes;
  long * arr;

  FILE *file = fopen(argv[1], "r");
  char* line = malloc(sizeof(char)*255);

  /* Ensure proper input file */
  if ((argc < 1) || (file == NULL)) {
    printf("usage: ./gattaca <in>\n");
    free(line);
    exit(1);
  }

  /* Load and parse input genes */
  fscanf(file, "%ld", &length);
  j = length % 80;
  if (j > 0) {
    fscanf(file, "%*s");
    length -= j;
  }
  for (i = 0; i < (length / 80) ; i++)
    fscanf(file, "%*s");
  length += j;
  fscanf(file, "%ld", &n);
  genes = malloc(n*sizeof(gene));
  if (genes == NULL)
    exit(1);
  for (i = 0; i < n; i++) {
    fscanf(file, "%ld%ld%ld", &x.start, &x.stop, &x.score);
    genes[i] = x;
  }
  fclose(file);

  /* Begin algorithm */
  quickSort(genes, 0, n - 1);

  arr = malloc((length + 2)*sizeof(long));
  arr[length+1] = 0;
  j = n-1;
  for (i = length; i > -1; i--) {
    arr[i] = arr[i+1];
    while (j > -1) {
      if (genes[j].start < i)
        break;
      else {
        if (arr[i] <= (genes[j].score + arr[genes[j].stop + 1]))
          arr[i] = genes[j].score + arr[genes[j].stop + 1];
        j--;
      }
    }
  }

  /* Print output and free data structures */
  printf("%ld\n", arr[0]);
  free(genes);
  return 0;
}
