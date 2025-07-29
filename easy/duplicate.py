#ARRAYS AND HASHING
#Date: July 29, 2025 00:14

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lst = []
        for num in nums:
            if num in lst:
                return True
            lst.append(num)
        return False
    
"""
brute force too common and would take too long
another method: convert nums to set and compare its length with original list length
takeaways: there are different ways to approach lists..can start by sorting them....can convert them into list to 
remove duplicates
"""