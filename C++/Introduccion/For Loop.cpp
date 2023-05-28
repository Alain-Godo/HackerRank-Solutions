#include <iostream>
#include <cstdio>
#include <map>
using namespace std;

int main() {
    int a,b;
    cin >> a >> b;
    map<int,string> numbers;
    numbers[1] = "one"; numbers[2] = "two";
    numbers[3] = "three"; numbers[4] = "four";
    numbers[5] = "five"; numbers[6] = "six";
    numbers[7] = "seven"; numbers[8] = "eight";
    numbers[9] = "nine";
    
    for(int i=a;i<=b;i++){
        if(i<=9 && i>=1){
            cout << numbers[i] << "\n";
        }
        else{
            cout << ((i&1)?"odd":"even") << "\n";
        }
    }
    return 0;
}