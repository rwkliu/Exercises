// Randomly swap the characters in string.
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

char *my_strfry(char *string) {
    if (string == NULL || strcmp(string, "") == 0) {
        return "";
    }
    size_t string_size = strlen(string);
    int last_index = string_size - 1;
    char *new_string = malloc(string_size + 1 * sizeof(char));
    time_t t1;
    srand((unsigned) time(&t1));
    int rand_index = 0;

    new_string = strcpy(new_string, string);

    for(int i = 0; i < string_size - 1; i++) {
        if (last_index == 0) {
            rand_index = 0;
        } else {
            rand_index = rand() % last_index;
        }
        
        char temp = new_string[last_index];
        new_string[last_index] = new_string[rand_index];
        new_string[rand_index] = temp;
        last_index--;
    }
    return new_string;

}

int main() {
    char *s1 = "abcdef";
    char *s2 = "aaaaaa";
    char *s3 = "";
    
    printf("%s\n", my_strfry(s1));
    printf("%s\n", my_strfry(s2));
    printf("%s\n", my_strfry(s3));

    return 0;
}