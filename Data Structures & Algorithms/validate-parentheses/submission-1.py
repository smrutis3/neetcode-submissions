class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char = {')' : '(', ']' :'[', '}':'{'} #hashmap(mapping closed bracket to open) 
        for c in s:
            if c in char:
                if stack and stack[-1] == char[c]:
                    stack.pop()
                else:
                    return False #parathesis don't match 
            else:
                stack.append(c) #open parathesis appended
        return True if not stack else False 




        while '()' in s or '{}' in s or '[]' in s:
            s=s.replace('()', '')
            s=s.replace('{}', '')
            s=s.replace('[]', '')
        return s == ''