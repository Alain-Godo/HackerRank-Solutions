#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <sstream>
using namespace std;


int main() {
    int n, q;
    cin >> n >> q;
    map<string,map<string,string> > tags;
    for(int i=1;i<=n;i++){
        string line;
        getline(cin,line);
        if( i<=(n/2) ){
            char aux; string tag_name;
            stringstream ss;
            ss << line;
            ss >> aux;
            ss >> tag_name;
            while(ss.rdbuf()->in_avail()){
                
            }
        }
    }  
    return 0;
}
