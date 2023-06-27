#include <iostream>
#include <unordered_map>

int firstUniqChar(std::string s) {
    std::unordered_map<char, int> countMap;

    // Count the frequency of each character in the  given string
    for (char ch : s) {
        countMap[ch]++;
    }

    // Find the first non-repeating character and return the index
    for (int i = 0; i< s.length(); i++) {
        if (countMap[s[i]] == 1) {
            return i;
        }
    }

    return -1; // return -1 if no non-repeating character found
}

int main() {
    std::string s = "leetcode";
    int index = firstUniqChar(s);
    std::cout << index << std::endl;

    return 0;
}
