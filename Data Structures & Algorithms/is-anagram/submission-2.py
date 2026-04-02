from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_composition = defaultdict(int)
        t_composition = defaultdict(int)

        for char_s in s:
            s_composition[char_s] += 1
        
        for char_t in t:
            t_composition[char_t] += 1


        return s_composition == t_composition