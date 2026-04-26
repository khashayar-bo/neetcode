#include <stdbool.h>

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string lcp = "";
        char currentLetter;
        int index = 0;
        while (true){
            if (index >= strs[0].size()) return lcp;
            currentLetter = strs[0][index];
            for (const string& str: strs) {
                if (index >= str.size() || str[index] != currentLetter) {
                    return lcp;
                }
            }
            index += 1;
            lcp += currentLetter;
        }
    }
};