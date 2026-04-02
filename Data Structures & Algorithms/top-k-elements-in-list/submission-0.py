class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = dict()

        for num in nums:
            count_dict[num] = 1 + count_dict.get(num, 0)
        
        topK = sorted(count_dict.items(), key=lambda item:item[1], reverse=True)[:k]

        return [top[0] for top in topK]