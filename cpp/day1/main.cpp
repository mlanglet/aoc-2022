#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main(){
    fstream file;
    file.open("../../input/day1",ios::in);
    if (file.is_open()){
        string line;
        int max = 0;
        int current = 0;
        int top1 = 0;
        int top2 = 0;
        int top3 = 0;
        while(getline(file, line)){
            if(line.compare("") == 0){
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
                current += std::stoi(line);
            }
        }

        printf("The most calories carried is %d\n", max);
        printf("The sum of calories carried by the three elves carrying the most is %d\n", (top1 + top2 + top3));

        file.close();
   }
}