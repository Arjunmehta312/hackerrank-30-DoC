#include <iostream>
using namespace std;

int main() {
    int returned_day, returned_month, returned_year;
    int due_day, due_month, due_year;
    
    // Input the returned date and due date
    cin >> returned_day >> returned_month >> returned_year;
    cin >> due_day >> due_month >> due_year;
    
    int fine = 0;

    if (returned_year > due_year) {
        fine = 10000;  // Fixed fine if returned after the expected year
    } else if (returned_year == due_year) {
        if (returned_month > due_month) {
            fine = 500 * (returned_month - due_month);  // Fine per month if within the same year but late in months
        } else if (returned_month == due_month && returned_day > due_day) {
            fine = 15 * (returned_day - due_day);  // Fine per day if within the same month but late in days
        }
    }

    cout << fine << endl;  // Output the calculated fine
    return 0;
}
