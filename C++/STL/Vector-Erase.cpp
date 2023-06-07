#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n; cin >> n;
    vector<int> v;
    for(int i=0;i<n;i++){
        int aux; cin >> aux;
        v.push_back(aux);
    }
    int n2;
    cin >> n;
    v.erase(v.begin()+(n-1));
    cin >> n >> n2;
    v.erase(v.begin()+(n-1),v.begin()+(n2-1));
    cout << v.size() << "\n";
    for(int i=0;i<v.size();i++){ cout<< v[i] << " "; }  
    return 0;
}
