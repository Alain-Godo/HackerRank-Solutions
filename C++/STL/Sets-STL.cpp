#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    int n; cin >> n;
    set<int> s;
    while(n--){
        int q,num;
        cin >> q >> num;
        switch (q) {
            case 1:
                s.insert(num);
                break;
            case 2:
                s.erase(num);
                break;
            case 3:
                cout << ((s.find(num)!=s.end())?"Yes":"No") << "\n";
                break;
        }
    }   
    return 0;
}
