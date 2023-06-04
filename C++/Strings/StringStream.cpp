#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
	stringstream ss(str);
    vector<int> auxiliar; int aux1; char aux2;
    while (ss.rdbuf()->in_avail()) {
        ss >> aux1;
        auxiliar.push_back(aux1);
        if(ss.rdbuf()->in_avail()){
            ss >> aux2;
        }
    }
    return auxiliar;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}