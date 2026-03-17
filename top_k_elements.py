"""
347. Top K Frequent Elements
given an array of integers, return the k most frequent elements.
key takeaway: use a dictionary to count the frequency of each element, and then use a list to store the top k elements.

"""
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        kfreq = []  #at  most will have length of k
        kstore = dict() #num:counter
        for num in nums:
            if num not in kstore:
                kstore[num] = 1
            else:
                kstore[num] += 1
            if len(kfreq) < k and num not in kfreq:
                kfreq.append(num)
            else:
                #only swap if num counter > kfreq num counter
                for i in range(len(kfreq)):
                    if num not in kfreq and kstore[num] > kstore[kfreq[i]]:
                        kfreq[i] = num
        return kfreq
        
        