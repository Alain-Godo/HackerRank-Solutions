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
    vector<string> hrml;
    vector<string> tags;
    map<string,string> tags_value;
    string line;
    cin >> ws;
    for(int i=0;i<n;i++){
        getline(cin,line);
        line.erase(remove(line.begin(),line.end(),'\"'),line.end());
        line.erase(remove(line.begin(),line.end(),'>'),line.end());

        if(line.substr(0,2) == "</"){
            tags.pop_back();
        }
        else{
            string prefix_tag = "";
            for(int j=0;j<tags.size();j++){
                prefix_tag += tags[j] + ".";
            }
            stringstream ss;
            ss << line;
            char aux;
            string tag,key,value;
            ss >> aux >> tag;
            tags.push_back(tag);
            while(ss){
                ss >> key >> aux >> value;
                tags_value[prefix_tag + tag + "~" + key] = value;
            }
        }
    }
    for(int i=0;i<q;i++){
        getline(cin,line);
        if(tags_value.find(line) != tags_value.end()){
            cout << tags_value[line] << "\n";
        }
        else{
            cout << "Not Found!\n";
        }
    }
    return 0;
}
