class Solution:
    def is_openning(self, c: str):
        openning = {'(', '[', '{'}
        
        return c in openning
    def is_match(self, first_c, second_c):
        matches = {'(': ')', '{': '}', '[': ']'}
        
        return matches[first_c] == second_c

    def isValid(self, s: str) -> bool:
        stack = list()


        for c in s:
            if self.is_openning(c):
                stack.append(c)
            else:
                if not stack:
                    return False

                if self.is_match(stack[-1], c):
                    stack.pop()
                else:
                    return False

        if len(stack) > 0:
            return False

        return True
