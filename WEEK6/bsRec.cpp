#include<iostream>
#include<vector>
using namespace std;

int bsRec(vector<int>&v, int s, int e, bool &isFound, int target){

    if(isFound || s > e) return -1;

    int mid = (s+e)/2;

    if(v[mid] == target){
        isFound = true;
        return mid;
    }

    else if(v[mid] > target){
        e = mid-1;
        bsRec(v, s, e, isFound, target);
    }

    else{
        s = mid+1;
        bsRec(v, s, e, isFound, target);
    }
}   

int main(){

    vector<int>v = {1,4,6,7,8,10,25,56,67,87,100};

    bool isFound = false;
    int ans = bsRec(v, 0, v.size()-1, isFound, 26);

    cout<<isFound<<": "<<ans<<endl;
}