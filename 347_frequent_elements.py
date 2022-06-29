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

# Another solution would be to use the bucket sort algorithm, creating an array with the lenght of the input array, then checking how many integers appear [index] times and adding them to the map. Finally we just need to return the k last numbers from highest index to lowest
from operator import itemgetter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1, 0 , -1):
            for n in freq[i]:
                res.append()
                if len(res) == k:
                    return res
