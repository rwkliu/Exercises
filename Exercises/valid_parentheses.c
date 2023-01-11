#include <stdio.h>
#include <stdbool.h>
#include <string.h>

//Return the index of the last opening bracket before a closing bracket
int last_open_bracket_index(char *input, int input_string_index) {
  int last_open_bracket_index = input_string_index;
  int index = input_string_index;

  while(input[index] != '\0') {
    if (input[index] == '}' || input[index] == ')' || input[index] == ']') {
      last_open_bracket_index = index - 1;
      return last_open_bracket_index;
    }
    index++;
  }
  return last_open_bracket_index;
}

//Return the corresponding closing bracket to the opening bracket
char closing_bracket(char opening_bracket) {
  if (opening_bracket == '(') {
    return ')';
  } else if (opening_bracket == '[') {
    return ']';
  } else if (opening_bracket == '{') {
    return '}';
  } else {
    return opening_bracket;
  }
}

//Determine if the input string is valid. The input string is valid if:
//1. Open brackets must be closed by the same type of brackets
//2. Open brackets must be closed in the correct order. Empty strings are also 
//considered valid
bool validParentheses(char *input) {
  int len = strlen(input);

  //Check edge cases
  if (len == 0) {
    return true;
  } else if (input[0] == ')' || input[0] == ']' || input[0] == '}' 
             || input[len] == '(' || input[len] == '[' || input[len] == '{') {
    return false;
  } else if (len % 2 != 0) {
    return false;
  }

  int index = 0;
  while (index < len) {
    int last_open_bracket = last_open_bracket_index(input, index);
    int index_offset = 1;
    for (int i = last_open_bracket; i >= index; i--) {
      if (closing_bracket(input[i]) != input[last_open_bracket + index_offset]) {
          return false;
      }
      index_offset++;
    }
    index += last_open_bracket + index_offset;
  }
  return true;
}

int main() {
  char *str1 = "()";
  char *str2 = "()[]{}";
  char *str3 = "(]";
  char *str4 = "([)]";
  char *str5 = "{[]}";

  printf("str1 expected result: %d\n", 1);
  printf("str1 actual result: %d\n", validParentheses(str1));
  printf("str2 expected result: %d\n", 1);
  printf("str2 actual result: %d\n", validParentheses(str2));
  printf("str3 expected result: %d\n", 0);
  printf("str3 actual result: %d\n", validParentheses(str3));
  printf("str4 expected result: %d\n", 0);
  printf("str4 actual result: %d\n", validParentheses(str4));
  printf("str5 expected result: %d\n", 1);
  printf("str5 actual result: %d\n", validParentheses(str5));
  
  return 0;
}
