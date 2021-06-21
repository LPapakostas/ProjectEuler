#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;

bool checkPan(vector<int> &x,vector<int> &y, vector<int> &pr){
    long int p1 = 0,p2 = 0,res = 0;
    for(size_t i = 0; i < x.size() ; ++i){
        p1 += x[i] * pow(10,i);
    }
    for(size_t i = 0; i < y.size() ; ++i){
        p2 += y[i] * pow(10,i);
    }
    for(size_t i = 0; i < pr.size() ; ++i){
        res += pr[i] * pow(10,i);
    }
    if(p1*p2==res) {cout << p1 << " * " << p2 << " = " << res << " "; return true;};
    return false;
}

vector<vector<int>> generateSol(){
    size_t i,j,k;
    vector<vector<int>> ret;
    vector<int> myDig = {1,2,3,4,5,6,7,8,9};
    long int iterDone = 0;
    do{
        for(i=0;i<myDig.size()-2;++i){
            for(j=i;j<myDig.size()-1;++j){
                vector<int> *x1 = new vector<int>(myDig.begin(),myDig.begin()+i);
                vector<int> *y1 = new vector<int>(myDig.begin()+i,myDig.begin()+j);
                vector<int> *z1 = new vector<int>(myDig.begin()+j,myDig.end());
                if( checkPan( *x1,*y1,*z1 ) ) {ret.push_back(*z1); cout << "at iteration " << iterDone << endl;};
                iterDone ++;
                delete x1,y1,z1;
            }
        }
    }while(next_permutation(myDig.begin(),myDig.end()));
    cout << "Total iterations : " << iterDone << endl;
    return ret;
}

bool crit(vector<int> &a, vector<int> &b){
    if(a[0]!=b[0]) return (a[0]>b[0]);
    else if(a[1]!=b[1]) return (a[1]>b[1]);
    else if(a[2]!=b[2]) return (a[2]>b[2]);
    else return ( a[3]>b[3]);
}

void printSum(vector<vector<int>> &d){
    long int sum = 0;
    int partsum = 0;
    for(size_t i = 0;i<d.size();++i){
        partsum = 0;
        for(size_t j = 0;j<(d[i]).size();++j){
            partsum += d[i][j]*pow(10,j);
        }
        sum+=partsum;
        if(i<d.size()-1) cout << "\t" << partsum << endl;
        else cout << "+\t" << partsum << endl;
    }
    cout << "\t-------\n\t" << sum << endl;
}

int main()
{
    vector<vector<int>>d = generateSol();
    cout << "Solutions found : " << d.size() << endl;
    sort(d.begin(),d.end(),crit);
    d.erase( unique(d.begin(),d.end()) , d.end() );
    cout << "Unique solutions found : " << d.size() << "\n" << endl;
    printSum(d);
}
