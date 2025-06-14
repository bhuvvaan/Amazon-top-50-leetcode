class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}

        for i, item in enumerate(nums):
            
            # first check if the item is in dict1 to avoid checking with itself
            # as usual take care if elements are in keys first
            if dict1 and item in dict1:
                return [dict1[item], i]
            
            dict1[target-item] = i
