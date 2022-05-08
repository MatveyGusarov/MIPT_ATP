#include <buffer.h>
#include <string>

void Buffer::Set(const std::string& other) {
    str_ = other;
}

std::string Buffer::Get() const {
    return str_;
}
