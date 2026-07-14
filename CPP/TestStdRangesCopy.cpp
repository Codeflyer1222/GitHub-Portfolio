#include <iostream>
#include <algorithm>
#include <vector>
#include <iterator>
using Path = std::vector<char>; // type alias for std::vector<char>

std::ostream& operator<< (std::ostream& out, const Path& v) {
    if ( !v.empty() ) {
        out << '[';
        std::ranges::copy(v, std::ostream_iterator<char>(out, ", "));
        out << "\b\b]"; // use two ANSI backspace characters '\b' to overwrite final ", "
    }
    return out;
}

int main() {
    Path path{'/', 'f', 'o', 'o'};

    // will output: "path: [/, f, o, o]"
    std::cout << "path: " << path << std::endl;

    return 0;
}