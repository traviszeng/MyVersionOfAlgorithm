#include<iostream>
using namespace std;

//ц╟ещеепР
extern void bubbleSort(int a[],int length) {
	for (int i = 0; i < length; i++) {
		for (int j = length-1; j >i; j--) {
			if (a[j] < a[j - 1]) {
				int temp = a[j];
				a[j] = a[j - 1];
				a[j - 1] = temp;
			}
		}
	}
	for (int i = 0; i < length; i++)
		cout << a[i] << " ";
	cout << endl;
}                                                                                                                                                                                                                     