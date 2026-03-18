"""
15. 3Sum
key takeaway: use two pointers to compare the sum of the two numbers and move ptrs accordingly
sorting allows for two pointer approach and also allows for easy skipping of duplicates
two pointer technique with a base and left and right ptrs


the below (commented out) is my initial attempt, passes but not efficient....
non commeneted is revised and checks for duplicates and is more efficient

"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            target = -nums[i]
            
            while l < r:
                tot = nums[l] + nums[r]
                if tot == target:
                    res.append([nums[i], nums[l], nums[r]])
                    #this only works because the array is sorted, we skip duplicates 
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    
                    l += 1
                    r -= 1
                    
                elif tot < target:
                    l += 1
                else:
                    r -= 1
        
        return res
    

    """
    class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        base = 0
        l = 1
        r = len(nums)-1
        lst = []
        
        while base <= len(nums)-3:
            target = 0 - nums[base]
            
            while l < r:
                tot = nums[l] + nums[r]
                if tot == target:
                    print(nums[base],nums[l],nums[r])
                    lst.append([nums[base],nums[l],nums[r]])
                    l+=1
                    r-=1
                elif tot < target:
                    l += 1
                    continue
                else:
                    r -= 1
                    continue
                
            base += 1
            l = base + 1
            r = len(nums)-1
        unique_lists = list(map(list, set(map(tuple, lst))))
        return unique_lists
        
                
                    
                

    """