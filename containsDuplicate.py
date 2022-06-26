# Statement:
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Solution:
# We could brute force by looping the array twice and look for the repetition, however a more efficient approach would be to create an auxiliar hashmap and look for the value there.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
