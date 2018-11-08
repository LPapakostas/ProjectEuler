#include <iostream>

using namespace std;

int main()
{
    int x1 = 1;
    int x2 = 1;
    int sum = 0;
    int temp;
    do{
        temp = x2;
        x2+=x1;
        x1 = temp;
        sum += (x2%2)?(0):(x2);
    }while(x2<4000000);
    cout << "Answer is : " << sum << endl;
}
