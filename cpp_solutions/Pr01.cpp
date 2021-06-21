#include <iostream>

using namespace std;

int main()
{
    int ans = 0;
    for(int i = 1;i<1000;++i) if( !(i%3) || !(i%5) ) ans+=i;
    cout << "Answer is : " << ans << endl;
}
