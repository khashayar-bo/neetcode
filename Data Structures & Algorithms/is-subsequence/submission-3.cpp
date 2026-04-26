class Solution {
public:
    bool isSubsequence(string s, string t) {
        int sIndex = 0;

        if (s == "") {
            return true;
        }

        for (int i=0; i < t.size(); i++) {
            if (t[i] == s[sIndex]) {
                sIndex++;

                if (sIndex == s.size()) {
                    return true;
                }
            }
        }

        return false;
    }
};