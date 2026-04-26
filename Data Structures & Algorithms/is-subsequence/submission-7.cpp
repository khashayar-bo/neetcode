class Solution {
public:
    bool isSubsequence(string& s, string& t) {
        if (s.empty()) return true;
        
        int sIndex = 0;
        int sSize = s.size();

        for (int i=0; i < t.size(); i++) {
            if (t[i] == s[sIndex]) {
                if (++sIndex == sSize) return true;
            }
        }

        return false;
    }
};