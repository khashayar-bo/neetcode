class Solution:
    def replaceElements(self, arr):
        max_val = -1

        for i in range(len(arr) - 1, -1, -1):
            new_max = max(arr[i], max_val)
            arr[i] = max_val
            max_val = new_max

        return arr
        