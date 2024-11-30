#include <iostream>
#include <fcntl.h>    // For open
#include <unistd.h>   // For read, close
#include <string>
#include <algorithm>
#include <cctype>
#include <cerrno>
#include <cstring>

char to_upper_char(char c) {
    return std::toupper(static_cast<unsigned char>(c));
}

int main() {
    const char* pipe_in = "input.pipe";

    // Open the named pipe for reading in non-blocking mode
    int fd = open(pipe_in, O_RDONLY | O_NONBLOCK);
    if (fd == -1) {
        std::cerr << "Error opening pipe '" << pipe_in << "': " << std::strerror(errno) << std::endl;
        return 1;
    }

    const size_t bufferSize = 1024;
    char buffer[bufferSize];
    ssize_t bytesRead;

    std::string line;
    while (true) {
        bytesRead = read(fd, buffer, bufferSize);
        if (bytesRead > 0) {
            for (ssize_t i = 0; i < bytesRead; ++i) {
                char c = buffer[i];
                if (c == '\n') {
                    std::transform(line.begin(), line.end(), line.begin(), to_upper_char);

                    std::cout << line << "\n";
                    line.clear();
                } else {
                    line += c;
                }
            }
        } else if (bytesRead == 0) {
            // No more data; writer has closed the pipe
            break;
        } else {
            if (errno == EAGAIN || errno == EWOULDBLOCK) {
                // No data available right now; wait or continue
                usleep(100000); // Sleep for 100ms
                continue;
            } else {
                std::cerr << "Error reading from pipe: " << std::strerror(errno) << std::endl;
                close(fd);
                return 1;
            }
        }
    }

    close(fd);
    return 0;
}
