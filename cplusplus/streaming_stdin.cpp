#include <iostream>
#include <string>

int main() {
    for (std::string line; std::getline(std::cin, line);)
        std::cout << "received " << line << "\n";

    return 0;
}
