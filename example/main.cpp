#include <bits/stdc++.h>

using namespace std;

int main() {
	int x1, r1, x2, r2;
	cin >> x1 >> r1 >> x2 >> r2;
	if (abs(x1 - x2) >= r1 + r2) {
		cout << 0;
	} else if (x2 - r2 <= x1 - r1 && x2 + r2 >= x1 + r1) {
		cout << 2;
	} else {
		cout << 1;
	}
	return 0;
}
