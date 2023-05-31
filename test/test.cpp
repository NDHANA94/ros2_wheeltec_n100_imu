#include <iostream>

using namespace std;




int main(int argc, char **argv){
    int count;
    std::cout << "\nCommand line args: \n";
    for (count = 0; count < argc; count++){
        cout << " argv[" << count << "]  " << argv[count] << "\n";
    }

}
