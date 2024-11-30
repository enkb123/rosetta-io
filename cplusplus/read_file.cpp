#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ifstream file("./my-text-file.txt");

    for (std::string line; std::getline(file, line); )
        std::cout << "line: " << line << "\n";

    return 0;
}
