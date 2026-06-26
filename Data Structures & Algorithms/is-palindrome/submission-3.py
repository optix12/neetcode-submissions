class Solution:
    def isPalindrome(self, s: str) -> bool:

        l = []
    
        for i in s:
            if i.isalnum() :
                l.append(i)
        return "".join(l).lower() == ("".join(l).lower() )[::-1]

                

        