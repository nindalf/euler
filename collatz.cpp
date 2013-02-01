#include <iostream>
#include <vector>
#include <map>

using namespace std;

map <int, int> precomputed;
int maximum;

int collatz_successor(int x)
{
	if(x%2 == 0)
		return x/2;
	else
		return 3*x + 1;
}

int collatz_length(int x)
{
	if(precomputed.count(x))
	{
		return precomputed[x];
	}
	else if(x > 1)
	{
		int successor = collatz_successor(x);
		int calc_length = 1 + collatz_length(successor);
		precomputed[x] = calc_length;
		return calc_length;
	}	

}

int main()
{
	precomputed.clear();
	precomputed[1] = 1;
	maximum = 1;
	for(int i = 2; i <= 1000000; i++)
	{
		collatz_length(i);
		if(precomputed[i] > precomputed[maximum])
			maximum = i;
	}
	cout << maximum << " " << precomputed[maximum] <<endl;

	return 0;
}
