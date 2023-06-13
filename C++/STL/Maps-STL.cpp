#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    int n; cin >> n;
    map<string,int> m;
    while(n--){
        string name;
        int q;
        cin >> q >> name;
        switch (q) {
            case 1: 
                int mark;
                cin >> mark;
                if(m.find(name) != m.end()){
                    m[name] += mark;
                }
                else{
                    m[name] = mark;
                }
                break;
                
            case 2:
                m.erase(name);
                break;
                
            case 3:
                cout << ((m.find(name) != m.end())?m[name]:0) << "\n";
                break;
        }
    }
    return 0;
}



