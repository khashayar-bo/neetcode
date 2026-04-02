class Solution:
    def _classify_str(self, string):
        result = [0 for i in range(26)]

        for char in string:
            char_index = ord(char) - ord('a')
            result[char_index] += 1 

        return ".".join(str(num) for num in result)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = {}
        for string in strs:
            string_group = self._classify_str(string)
            if string_group not in anagram_groups:
                anagram_groups[string_group] = []

            anagram_groups[string_group].append(string)

        return list(anagram_groups.values())