//Program 1.14: permutation using the STL algorithm next_permutation
#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
using namespace std;

void Permutations(char* a, const int m)
{

	do {
		copy(a, a + m + 1, ostream_iterator<char>(cout, ""));
		cout << endl;
	} while (next_permutation(a, a + m + 1));
}
