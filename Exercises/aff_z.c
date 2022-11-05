// aff_z takes a string, and print the first 'z'
// character it encounters, followed by a newline. If there are no
// 'z' characters in the string, the program writes 'z' followed
// by a newline. If the number of parameters is not 1, the program prints
// 'z' followed by a newline.
#include <stdio.h>

int my_string_index(char* param_1, char param_2){
  int index = 0;

  while (*param_1) {
    if(*param_1 == param_2) {
        return index;
    }
    index++;
    param_1++;
  }
  return -1;
}

void aff_z(char *str) {
  if(str == "") {
    printf("z\n");
  }
  else if(my_string_index(str, 'z') == -1) {
    printf("z\n");
  }
}

int main() {
  char *str1 = "abc";
  char *str2 = "RaInB0w d4Sh!";
  char *str3 = "";

  aff_z(str1);
  aff_z(str2);
  aff_z(str3);

  return 0;
}