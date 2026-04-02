class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_pointer = 0
        right_pointer = 1
        current_len = 0
        best_len = 0
        current_chars = set()

        while right_pointer <= len(s):
            new_char = s[right_pointer - 1]

            while new_char in current_chars:
                current_chars.remove(s[left_pointer])
                current_len -= 1
                left_pointer += 1

            current_chars.add(new_char)
            current_len += 1
            best_len = max(best_len, current_len)

            right_pointer += 1

        return best_len
