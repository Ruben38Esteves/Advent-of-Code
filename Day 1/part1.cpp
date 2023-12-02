#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main(){
    ifstream file("part1.txt");
    string line,num;
    int sum = 0;
    char first,last;
    bool firstFound;
    while(getline(file, line)){
        firstFound = false;
        for(char c : line){
            if(isdigit(c)){
                if(!firstFound){
                    first = c;
                    firstFound = true;
                }
                last = c;
            }
        }
        num = string(1, first) + string(1, last);
        sum += stoi(num);
    }
    cout << sum << endl;
}