#include <iostream>
#include <vector>
#include "functions.hpp"

using namespace std;

vector<float> computationOfBasis(vector<float> nodes, vector<float> f_values, int size);
float newtonInterpolation(vector<float> nodes, vector<float> basis, int size, float input);




int main(void)
{
	float input, result;
	vector<float> nodes, f_values, basis;
	
	cout << "Input value for interpolaction: ";
	cin  >> input;
	
	nodes = functions::loadFromFile("2_newton.txt", f_values);
	
	basis  = computationOfBasis(nodes, f_values, nodes.size());
	result = newtonInterpolation(nodes, basis, nodes.size(), input);
	
	for(float param: basis){
		cout << param << " ";
	}
	cout << "\nResult : " << result << endl;
}




vector<float> computationOfBasis(vector<float> nodes, vector<float> f_values, int size){
	vector<float> temp = f_values;
	
	for(int i = 1; i < size; ++i){
		for (int j = 0; j < i; ++j){
			
	            temp[i] = (temp[i] - temp[j]) / (nodes[i] - nodes[j]);
	    }
	}

	return temp;
}


float newtonInterpolation(vector<float> nodes, vector<float> basis, int size, float input){
	float result = basis[0];
	float temp   = 1.0;
	
	for(int i = 1; i < size; ++i){
		for(int j = 0; j < i; ++j){
			
			temp *= (input - nodes[j]);
		}
		
		result += temp * basis[i];
		temp    = 1.0;
	}
	
	return result;
}
