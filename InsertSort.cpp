#include<iostream>
using namespace std;
extern int insertSort(int a[],int const length) {

	cout << length<<endl;
	for (int j = 1; j < length; j++) {
		int key = a[j];
		//insert a[j] into the sorted array a[1..j-1]

		int i = j - 1;
		while (i >=0 && a[i] > key) {
			a[i + 1] = a[i];
			i = i - 1;
		}
		a[i + 1] = key;
	}

	for (int i = 0; i < length; i++) {
		cout << a[i] << " ";
	}
	cout << endl;

	return 0;
}