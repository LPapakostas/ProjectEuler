#include <iostream>
#include <math.h>

using namespace std;

bool isPrime(long int &x){
    if(!(x%2)&&(x>2)) return false;
    for(long int i=3;i<=sqrt(x);i+=2) if(!(x%i)) return false;
    return true;
}

int main()
{
    long int num = 600851475143;
    long int fact = 2;
    for(long int i = 3; i <=  num/2; i+=2) if(!(num%i)) if(isPrime(i)) {fact = i; cout << "Found : " << i << "\nSearching..." << endl;}
    cout << ">> Solution is : " << fact << " !!" << endl;
}
