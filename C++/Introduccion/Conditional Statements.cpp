#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);



int main()
{
    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));
    map<int,string> numbers;
    numbers[1] = "one"; numbers[2] = "two";
    numbers[3] = "three"; numbers[4] = "four";
    numbers[5] = "five"; numbers[6] = "six";
    numbers[7] = "seven"; numbers[8] = "eight";
    numbers[9] = "nine";
    
    if(n<=9){
        cout << numbers[n];
    }
    else{
        cout << "Greater than 9";
    }

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
