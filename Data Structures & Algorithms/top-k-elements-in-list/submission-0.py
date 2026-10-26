class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)     #counts the number of times elements that appear in the list 
        return [num for num, freq in count.most_common(k)]
        
        #most_common() method returns the elements and their frequencies, sorted from highest frequency to lowest.