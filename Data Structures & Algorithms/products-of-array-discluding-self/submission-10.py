class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                zero_count += 1

        if zero_count > 1:
            return [0 for i in range(len(nums))]

        if zero_count == 1:
            result = [0 for i in range(len(nums))]
            result[nums.index(0)] = product
            return result

        for i in range(len(nums)):
            nums[i] = int(product /nums[i])

        return nums