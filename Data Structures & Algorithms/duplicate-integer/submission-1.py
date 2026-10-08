class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

        #TC
        #O(N): iterates through every element in nums
        #SC
        #O(N): total count of unqiue numbers in our seen set(worst case: all numbers are      unqiue in nums)
