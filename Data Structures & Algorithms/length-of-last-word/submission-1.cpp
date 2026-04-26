class Solution {
public:
    int lengthOfLastWord(string s) {
      int startingIndex = s.size() - 1;
      while (s[startingIndex] == ' ') {
        startingIndex--;
      }

      int currentIndex = startingIndex;
      while (s[currentIndex] != ' ' && currentIndex >= 0) {
        currentIndex--;
      }

     return startingIndex - currentIndex;
    }
};