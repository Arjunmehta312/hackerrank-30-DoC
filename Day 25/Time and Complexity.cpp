#include <cmath>
#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        bool isPrime = true;

        if (n <= 1) {
            isPrime = false;
        } else if (n <= 3) {
            isPrime = true;
        } else if (n % 2 == 0 || n % 3 == 0) {
            isPrime = false;
        } else {
            for (int i = 5; i * i <= n; i += 6) {
                if (n % i == 0 || n % (i + 2) == 0) {
                    isPrime = false;
                    break;
                }
            }
        }

        if (isPrime) {
            cout << "Prime" << endl;
        } else {
            cout << "Not prime" << endl;
        }
    }
    return 0;
}
