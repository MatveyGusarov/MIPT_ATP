#pragma once
#include <string>

class Buffer {
 public:
    void Set(const std::string& other);
    std::string Get() const;
 private:
    std::string str_;
};
