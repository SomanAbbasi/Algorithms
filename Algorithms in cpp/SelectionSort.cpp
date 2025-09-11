#include <iostream>
using namespace std;

int main() {
    int arr[5] = {1, 2, 5, 4, 3};
    int n = 5;

    for (int i = 0; i < n - 1; i++) {
        int index = i; // Assume current i is min

        // Find the index of the minimum element
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[index]) {
                index = j;
            }
        }

        // Swap the found minimum with arr[i]
        if (index != i) {
            int temp = arr[i];
            arr[i] = arr[index];
            arr[index] = temp;
        }
    }

    cout << "Selection Sort: ";
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
