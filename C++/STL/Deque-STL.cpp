#include <iostream>
#include <deque> 
#include <algorithm>
using namespace std;

void printKMax(int arr[], int n, int k){
	deque<int> dq;
    
    for(int i=0;i<n;i++){
        if(dq.size() < k){
            dq.push_front(arr[i]);
        }
        else{
            dq.pop_back();
            dq.push_front(arr[i]);
        }
        if(dq.size() == k){
            cout << *(max_element(dq.begin(),dq.end())) << " "; 
        }
    }
    cout << "\n";
}

int main(){
  
	int t;
	cin >> t;
	while(t>0) {
		int n,k;
    	cin >> n >> k;
    	int i;
    	int arr[n];
    	for(i=0;i<n;i++)
      		cin >> arr[i];
    	printKMax(arr, n, k);
    	t--;
  	}
  	return 0;
}