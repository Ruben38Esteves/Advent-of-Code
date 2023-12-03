#include <iostream>
#include <bits/stdc++.h>
using namespace std;

unordered_map<string, char> numberMap = {
    {"one", '1'},
    {"two", '2'},
    {"three", '3'},
    {"four", '4'},
    {"five", '5'},
    {"six", '6'},
    {"seven", '7'},
    {"eight", '8'},
    {"nine", '9'}
};

bool canItBeANumber(string word){
    for(const auto& [key, value] : numberMap){
        if(key.find(word) != string::npos){
            return true;
        }
    }
    return false;
}

char getNumberFromString(string word){
    string newword;
    int i = word.length()-1;
    int h = word.length()-1;
    while(i > 0){
        newword = string(1, word[i]);
        h = i;
        while(canItBeANumber(newword)){
            if(numberMap.find(newword) != numberMap.end()){
                return numberMap[newword];
            }
            h--;
            newword = string(1, word[h]) + newword;
        }
        i--;
    }
    return 'a';
}

char getFirstNumberFromString(string word){
    string newword;
    int k = 0;
    int j = 0;
    while(k < word.length()){
        newword = string(1, word[k]);
        j=k;
        while(canItBeANumber(newword)){
            if(numberMap.find(newword) != numberMap.end()){
                return numberMap[newword];
            }
            j++;
            newword += string(1, word[j]);
        }
        k++;
    }
    return 'a';
}

int main(){
    ifstream file("part1.txt");
    string line,num,word;
    int sum = 0;
    char first,last,previousc,wordc;
    bool firstFound;
    int n = 1;
    while(getline(file, line)){
        previousc = ' ';
        firstFound = false;
        word="";
        for(char c : line){
            if(isdigit(c)){
                wordc = getNumberFromString(word);
                if(wordc != 'a'){
                    if(!firstFound){
                        first = getFirstNumberFromString(word);
                        firstFound = true;
                    }
                    last = wordc;
                }
                if(!firstFound){
                    first = c;
                    firstFound = true;
                }
                last = c;
                word=previousc;
            }else{
                word += string(1, c);
                previousc = c;
            }
        }
        wordc = getNumberFromString(word);
        if(wordc != 'a'){
            if(!firstFound){
                first = getFirstNumberFromString(word);
                firstFound = true;
            }
            last = wordc;
        }
        num = string(1, first) + string(1, last);
        n++;
        sum += stoi(num);
    }
    cout << sum << endl;
}