#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    FILE* fp;
    char* line = NULL;
    size_t len = 0;

    fp = fopen("../../input/day1", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    int max = 0;
    int current = 0;
    int top1 = 0;
    int top2 = 0;
    int top3 = 0;
    while (getline(&line, &len, fp) != -1) {
        if(strcmp(line, "\n") == 0){
            if(current > max){
               max = current;
            }

            if(current > top1){
                top3 = top2;
                top2 = top1;
                top1 = current;
            } else if(current > top2){
                top3 = top2;
                top2 = current;
            } else if(current > top2){
                top3 = current;
            }

            current = 0;
        } else {
            current += atoi(line);
        }
    }

    printf("The most calories carried is %d\n", max);
    printf("The sum of calories carried by the three elves carrying the most is %d\n", (top1 + top2 + top3));

    fclose(fp);
    free(line);
    exit(EXIT_SUCCESS);
}