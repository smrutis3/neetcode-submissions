class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in count:
                return False 

            count[char] -= 1

            if count[char] < 0:
                return False

        return True

        #using counter((hashmap counting characters))
        #TC
        #O(N): length of string s and t
        #SC
        #O(1) OR O(K): where K is size of the unqiue character in the string