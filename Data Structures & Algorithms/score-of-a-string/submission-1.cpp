#include <cmath>

class Solution {
public:
    int scoreOfString(string s) {
        int score = 0;
        for (int i=0; i < s.size() - 1; i++) {
            score += std::abs(static_cast<int>(s[i+1]) - static_cast<int>(s[i]));
        }

        return score;
    }
};