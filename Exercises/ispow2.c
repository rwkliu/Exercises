//Determine if a number is a power of 2, 1 if true, else 0
//Methodology
//1. If n ends in 1, 4, 5, 6, 9, or 00, go to step 2.
//2. If the digital root of n equals 0, 1, 4, or 7, return 1
#include <stdio.h>

int digital_root(long int n) {
  int digital_root = 0;
  while(n > 9) {
    digital_root += n % 10;
    n = n / 10;
  }
  return digital_root;
}

int is_power_of_2(long int n) {
  int lsb = n % 10;
  int end[5] = {1, 4, 5, 6, 9};
  int dig_roots[4] = {0, 1, 4, 7};

  for(int i = 0; i < 5; i++) {
    if(n == 0 || n == 1) {
      return 0;
    }
    else if(lsb == end[i] || n % 100 == 0) {
      for(int j = 0; j < 4; j++) {
        if(digital_root(n) == dig_roots[j]) {
          return 1;
        }
      }
    }
  }
  return 0;
}

int main() {
  int n1 = 0;
  int n2 = 1;
  int n3 = 4;
  long int n4 = 4294967295;

  printf("%d\n", is_power_of_2(n1));
  printf("%d\n", is_power_of_2(n2));
  printf("%d\n", is_power_of_2(n3));
  printf("%d\n", is_power_of_2(n4));
  return 0;
}