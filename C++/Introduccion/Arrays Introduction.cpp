#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n, q;
    cin >> n >> q;
    vector<vector<int>> obj;
    obj.assign(n,vector<int>());
    
    int aux1,aux2;
    for(int i=0;i<n;i++){
       cin >> aux1;
       for(int j=0;j<aux1;j++){
           int axu2; cin >> aux2;
           obj[i].push_back(aux2);
       } 
    }
    
    for(int i=0;i<q;i++){
        cin >> aux1 >> aux2;
        cout << obj[aux1][aux2] << "\n";
    }
    return 0;
}