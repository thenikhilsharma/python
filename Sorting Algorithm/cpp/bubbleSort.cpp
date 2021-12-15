#include <iostream>
using namespace std;

int* bubbleSort(int arr[], int size) {

    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                int a = arr[j];
                int b = arr[j+1];
                arr[j] = a;
                arr[j+1] = b;
            }
        }
    }

    return arr;
}
int main() {

    int len;    //input length of array
    cin >> len;
    int arr[len];

    //For input an array
    for (int i=0; i<len; i++) {
        cin >> arr[i];
    }

    int* sort = bubbleSort(arr, len);

    // For printing an array
    for (int i = 0; i < 5; ++i) {
        cout << sort[i] << ", ";
    }

    return 0;
}