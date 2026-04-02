class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        results = {}
        nums_set = set(nums)
        starting_positions = set()
        longest_seq = 0

        for num in nums:
            if num - 1 not in nums_set:
                starting_positions.add(num)

        for starting_position in starting_positions:
            last_number = starting_position
            current_seq = 1
            while last_number + 1 in nums_set:
                current_seq += 1
                last_number += 1
            if current_seq > longest_seq:
                longest_seq = current_seq

        
        return longest_seq

        