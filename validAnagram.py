# Statement
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Solution:
# We need to create two hashmaps, each one containing the number of letters that appear on each string, this way, if we compare the two hashmaps and t has the same letter appearing at the same rate, then t is an anagram of s.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counterS, counterT = {}, {}


        for i in range(len(s)):
            counterS[s[i]] = 1 + counterS.get(s[i], 0)
            counterT[t[i]] = 1 + counterT.get(t[i], 0)

        for c in counterS:
            if counterS[c] != counterT.get(c, 0):
                print(counterS)
                print(counterT)
                return False
        return True
