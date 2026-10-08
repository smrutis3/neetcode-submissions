class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        #i for index, num is for the value
        for i, num in enumrate(nums):
            complement = target - num 

            if complement in seen:
                return (seen[complement], i)
            seen[num] = i 

        return []
        