#include <iostream>
#include <vector>
#include "functions.hpp"

using namespace std;


float lagrandeInterpolation(vector<float> nodes, vector<float> f_values, int size, float input);




int main(void)
{
	float input, result;
	vector<float> nodes, f_values;
	
	cout << "Input value for interpolaction: ";
	cin  >> input;
	
	nodes = functions::loadFromFile("1_lagran.txt", f_values);
	
	result = lagrandeInterpolation(nodes, f_values, nodes.size(), input);
	
	cout << "\nResult : " << result << endl;
}




float lagrandeInterpolation(vector<float> nodes, vector<float> f_values, int size, float input){
	float result = 0.0;
	float temp   = 1.0;
	
	for(int i = 0; i < size; ++i){
		for(int j = 0; j < size; ++j){
			if(i == j){
				continue;
			}
			
			temp *= (input - nodes[j]) / (nodes[i] - nodes[j]);
		}
				
		result += temp * f_values[i];
		temp    = 1.0;
	}
	
	return result;
}
