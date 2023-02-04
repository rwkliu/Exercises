//You are given an integer array gain of length n where gain[i] is the net gain
//in altitude between points i and i+1 fpor all (0 <= i < n). Return the 
//highest altitude of a point.

#include <stdio.h>

int largest_altitude(int *gain, int num_alts) {
  int highest = 0;
  int current_alt = 0;

  for (int i = 0; i < num_alts; i++) {
    if ((current_alt += gain[i]) > highest) {
      highest = current_alt; 
    }
  }
  return highest;
}

int main() {
  int gain1[5] = {-5, 1, 5, 0, -7};
  int gain2[7] = {-4, -3, -2, -1, 4, 3, 2};

  printf("highest altitude in gain1: %d\n", largest_altitude(gain1, 5));
  printf("highest altitude in gain2: %d\n", largest_altitude(gain2, 7));
  return 0;
}
