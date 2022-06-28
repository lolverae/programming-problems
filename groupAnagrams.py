# Statement:
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.'

# Solution:
# As a brute force approach we could sort every string inside the array and check for equality on each string
# A simpler solution would be to create a hashmap per each string on the array and check for valid anagrams inside the general map 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()i
