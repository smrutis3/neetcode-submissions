class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        #i for index, num is for the value
        for i, nums in enumerate(nums):
            complement = target - nums 

            if complement in seen:
                return [seen[complement], i]
            seen[nums] = i 

        return []

        #TIME COMPLEXITY
        #O(N) : WHERE N IS NUMBER OF ELEMENTS IN THE ARRAY
        #SPACE COMPLEXITY
        #O(N) : WHERE N IS KEY VALUE PAIRS STORED IN HASHMAP(SEEN)