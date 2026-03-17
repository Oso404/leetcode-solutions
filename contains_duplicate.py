"""
217. Contains Duplicate
key takeaway: use a set to check for duplicates 
"""
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
       return len(nums) != len(set(nums))
