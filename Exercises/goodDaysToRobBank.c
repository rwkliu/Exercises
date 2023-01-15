/*You are given a 0-indexed integer array security, where security[i] is the number of guards on duty on the ith day. The days are numbered starting from 0. You are also given an integer time.
The ith day is a good day to rob the bank if:
There are at least time days before and after the ith day,
The number of guards at the bank for the time days before i are non-increasing, and
The number of guards at the bank for the time days after i are non-decreasing.
*/
#include <stdio.h>
#include <stdlib.h>

int *index_list(int array_length) {
  int *result = malloc(array_length * sizeof(int));

  for (int i = 0; i < array_length; i++) {
    result[i] = i;
  }
  return result;
}

int *good_days_to_rob_bank(int *security, int *result_length, int length, int time) {
  int *result = NULL;
  int result_index = 0;
  int *curr = NULL;
  int *next = NULL;
  int window = length - time - 1;

  //check edge cases
  if (time == 0) {
    *result_length = length;
    result = index_list(length);
    return result;
  } else if (length == 0 || length <= 2 * time) {
    return NULL;
  }

  result = malloc(length * sizeof(int));
  curr = &security[0];
  next = &security[1];

  for (int i = time; i < length - time; i++) {
    if (i <= window && *curr >= *next) {
      curr = &security[i + 1];
      next = &security[i + 2];
      if (*curr <= *next) {
        result[result_index] = i;
        curr = &security[i - 1];
        next = &security[i];
        (*result_length)++;
        result_index++;
      }
    } else if (i <= window && !(*curr >= *next)) {
      curr = &security[i - 1];
      next = &security[i];
      continue;
    }
  }

  return result;
}

void print_list(int *array, int array_length) {
  int index = 0;

  printf("[");
  while(index < array_length) {
    printf("%d", array[index]);
    if (index != array_length - 1) {
      printf(",");
    }
    index++;
  }
  printf("]\n");
}

int main() {
  int result_length1 = 0;
  int result_length2 = 0;
  int result_length3 = 0;

  int security1[] = {5,3,3,3,5,6,2};
  int length1 = sizeof(security1)/sizeof(security1[0]);
  int time1 = 2;
  int *result1 = good_days_to_rob_bank(security1, &result_length1, length1, time1);
  printf("result1\n");
  print_list(result1, result_length1);

  int security2[] = {1,1,1,1,1};
  int time2 = 0;
  int length2 = sizeof(security2)/sizeof(security2[0]);
  int *result2 = good_days_to_rob_bank(security2, &result_length2, length2, time2);
  printf("result2\n");
  print_list(result2, result_length2);

  int security3[] = {1,2,3,4,5,6};
  int time3 = 2;
  int length3 = sizeof(security3)/sizeof(security3[0]);
  int *result3 = good_days_to_rob_bank(security3, &result_length3, length3, time3);
  printf("result3\n");
  print_list(result3, result_length3); 
  
  return 0;
}
