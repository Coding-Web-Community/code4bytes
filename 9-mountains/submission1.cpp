//Written by Manish#9999

#include <bits/stdc++.h>
using namespace std;

int main(){
	int a[] = {9, 8, 8, 7, 9, 8, 10, 9, 11, 10, 10, 9, 9, 8, 10, 7, 11, 8, 12, 9, 11, 10, 10, 9, 9, 8, 8, 9, 7, 8, 6};
	int len = sizeof(a)/sizeof(*a);
	for(int i=0; i<len; i++){
		if (i==0 || i == len-1) continue;
		if (a[i] > a[i-1] && a[i] > a[i+1]) cout << i << " ";
	}
	return 0;
}
