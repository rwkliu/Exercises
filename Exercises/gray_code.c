// An n-bit gray code sequence is a sequence of 2n integers where:
// 1 <= n <= 16
// Every integer is in the inclusive range [0, 2n - 1],
// The first integer is 0,
// An integer appears no more than once in the sequence,
// The binary representation of every pair of adjacent integers differs by exactly one bit, and
// The binary representation of the first and last integers differs by exactly one bit.
// Given an integer n, return any valid n-bit gray code sequence.

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int one_bit_difference(int a, int b) {
  int bit_diff = (a ^ b) % 2;
  if(bit_diff == 1) {
    return 0;
  }
  else {
    return 1;
  }
}

// int get_last_integer(int n) {
//   int last_integer[5] = {1, 2, 4, 8, 16};
//   time_t t1;
//   int i;
//   srand((unsigned)time(&t1));
//   int last_int_index = rand() % 5;

//   while(last_integer[last_int_index] > n) {
//     last_int_index = rand() % 5;
//   }

//   return last_integer[last_int_index];
// }

int *grayCode(int n, int *returnSize) {
  int length = 2 * n;
  int *output = calloc(length, sizeof(int));
  // int last_int = get_last_integer(n);

  for(int i = 0; i < length; i++) {
    // if(i == last_int) {
    //   output[i] = 2 * n - 1;
    //   output[length -1] = last_int;
    //   continue;
    // }
    output[i] = i;
  }

  for(int i = 0; i < length; i++) {
    output[i] ^= output[i] >> 1;
    printf("%d\n", output[i]);
  }

}

int main(int argc, char **argv) {
  int n = atoi(argv[1]);
  grayCode(n, NULL);
  return 0;
}