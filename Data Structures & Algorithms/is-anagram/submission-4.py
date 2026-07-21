from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        w1 = dict(Counter(s))
        w2 = dict(Counter(t))
        if(w1 == w2):
            return True

        return False;
