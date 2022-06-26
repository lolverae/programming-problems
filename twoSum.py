# Statement:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target

# Solution:
# The initial approach would be to brute force the whole array looking for the value which sum equals the target, this is O(n^2)
# A more efficient approach would be to create an auxiliar hashmap and look if the value that, summed with the current value, gives me the target value.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         res = nums[i]+nums[j]
        #         if res == target:
        #             solution = [i, j]
        #             return solution   
        
        solmap = {} # val -> index
        for i, n in enumerate(nums):
            res = target - n
            if res in solmap:
                return [solmap[res], i]
            solmap[n] = i

