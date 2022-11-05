#include <stdio.h>
#include <stdlib.h>

#ifndef STRUCT_STRING_ARRAY
#define STRUCT_STRING_ARRAY 
typedef struct s_string_array {
  char *string;
  int integer;
} string_integer;
#endif

#ifndef STRUCT_STRING_INTEGER_ARRAY
#define STRUCT_STRING_INTEGER_ARRAY
typedef struct s_string_integer_array {
  int size;
  string_integer **array;
} string_integer_array;
#endif

float my_average_mark(string_integer_array *grades) {
  float average;
  float sum = 0.0;

  for(int i = 0; i < grades->size; i++) {
    sum += grades->array[i]->integer;
  }
  average = sum / grades->size;
  return average;
}

int main() {
  string_integer_array *grades = malloc(sizeof(string_integer_array));
  grades->size = 4;
  grades->array = malloc(grades->size *sizeof(string_integer *));

  grades->array[0] = malloc(sizeof(string_integer));
  grades->array[1] = malloc(sizeof(string_integer));
  grades->array[2] = malloc(sizeof(string_integer));
  grades->array[3] = malloc(sizeof(string_integer));

  grades->array[0]->string = "John";
  grades->array[0]->integer = 7;
  grades->array[1]->string = "Margot";
  grades->array[1]->integer = 8;
  grades->array[2]->string = "Jules";
  grades->array[2]->integer = 4;
  grades->array[3]->string = "Marco";
  grades->array[3]->integer = 19;

  float average = my_average_mark(grades);

  printf("Average: %0.2f\n", average);

  return 0;
}