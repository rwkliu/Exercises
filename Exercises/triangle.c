#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Print a triangle made of stars. n determines the number of rows
void triangle(int n) {
  char *row = malloc(n * sizeof(char));
  *row = '*';
  for(int i = 1; i <= n; i++) {
      printf("%s\n", row);
      row[i] = '*';
  }
  free(row);
}

void pyramid(int n) {
  char *row = malloc((2 * n - 1) * sizeof(char));
  char *spaces = malloc((n - 1) * sizeof(char));
  char *head = spaces;

  *row = '*';
  for(int i = 0; i < (n - 1); i++) {
      spaces[i] = ' ';
  }
  spaces[n] = '\0';
  for(int i = 0; i < n; i++) {
      printf("%s%s\n", spaces, row);
      spaces++;
      strcat(row, "**");
  }
  free(row);
  free(head);
}

int main() {
  // triangle(4);
  pyramid(4);
  return 0;
}