class Solution {
public:
    int appendCharacters(string s, string t) {
        if (t.empty()) return 0;
        
        int tIndex = 0;
        int tSize = t.size();

        for (int i=0; i < s.size(); i++) {
            if (s[i] == t[tIndex]) {
                tIndex++;
            }
        }

        return tSize - tIndex;
    }
};