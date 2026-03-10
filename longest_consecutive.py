"""
128. Longest Consecutive Sequence
key takeaway: use a set for O1 lookup time, and only start counting from a start sequence
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # ml = 0
        # store = dict()
        # for num in nums:
        #     if(num-1 not in store):
        #         store[num] = [num]
        #     else:
        #         store[num-1].append(num)
        #         store[num] = store.pop(num-1)
        #     if len(store) > ml:
        #         ml = len(store)
        # return ml
        s = set(nums) #set lookup time is o(1)
        longest = 0
        for num in nums:
            if num-1 in s:
                continue
            else:
                curr_max = 1 
                while num + curr_max in s:
                    curr_max += 1

            longest = max(longest,curr_max)
            

        return longest
