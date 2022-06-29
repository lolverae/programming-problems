# Statement:
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Solution:
# We could create a hashmap with the count of each integer on the given array, then sort that dictionary and return k numbers on the sorted dictionary, since this approach uses a sort function, this has a complexity of O(nlog(n)) 

from operator import itemgetter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for n in nums:
            if(n in freq):
                freq[n] += 1
            else:
                freq[n] = 1
        
        res = dict(sorted(freq.items(), key = itemgetter(1), reverse = True)[:k])
        values = res.keys()
        values_list = list(values)
        return values_list
