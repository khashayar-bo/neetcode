class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        mapp = {}
        for i, num in enumerate(nums):
            mapp[num] = i
        result = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                current_sum = nums[i] + nums[j]
                needed_num = -1 * current_sum
                k = mapp.get(needed_num)

                if k and k > j:
                    result.add(tuple(sorted((nums[i],nums[j],nums[k]))))
        
        return [list(res) for res in result]
