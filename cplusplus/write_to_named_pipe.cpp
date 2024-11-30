#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::string outFile = "output.pipe";
    std::string text = "Hello World!";

    std::ofstream file(outFile, std::ios::out | std::ios::binary);

    file.write(text.c_str(), text.size());
    file.close();

    return 0;
}
