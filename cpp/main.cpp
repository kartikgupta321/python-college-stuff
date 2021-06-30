# include<iostream>
#include<iomanip>
using namespace std;
int main(){
    int const a=10, & b=a;
    cout<<setw(3)<<b<<endl;
    cout<<setw(6)<<b;
}