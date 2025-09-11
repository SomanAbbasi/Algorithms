#include <iostream>
#include <vector>
#include <algorithm> // for swap func.
using namespace std;

// Bubble Sort function
void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    bool swapped;

    for (int i = 0; i < n - 1; i++) {
        swapped = false;

        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }

        // If no two elements were swapped, break
        if (!swapped) break;
    }
}

int main() {
    vector<int> arr = {5, 4, 2, 1, 3};

    bubbleSort(arr);

    cout << "Bubble Sorted Array: ";
    for (int x : arr) {
        cout << x << " ";
    }
    cout << endl;

    return 0;
}
