#ifndef FUNCTIONS_H_
#define FUNCTIONS_H_

#include <string>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <vector>

using namespace std;




namespace functions
{
	
	vector<float> loadFromFile(string fileName, vector<float>& vec2){
		vector<float> vec;
		ifstream file;
		string   line, str;
		float	 number;
	
		file.open(fileName, ios::in);
		if(file.good() == false){
			return vec;
		}
	
		getline(file,line);
		stringstream ss(line);
	
		while(!ss.eof()){
			ss >> str;
				
			if(stringstream(str) >> number){
				vec.push_back(atof(str.c_str()));
			}
			str = "";
		}
	
		getline(file,line);
		stringstream sss(line);
	
		while(!sss.eof()){
			sss >> str;
				
			if(stringstream(str) >> number){
				vec2.push_back(atof(str.c_str()));
			}
			str = "";
		}
	
		file.close();
		return vec;
	}
	
}


#endif /* FUNCTIONS_H_ */