#Product of Array Except Self
"""
key takeaway: prefix & suffix allows us to calculate all except self
think "prefix" and "suffix" whenver we see "except self" or "except current index"
"""
class Solution:

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        products = [1] * len(nums)
        mult = 1
        for i in range(1,len(nums)):
            mult *= nums[i-1]
            products[i] = mult
        mult = 1
        nums.reverse()
        for i in range(1,len(nums)):
            mult *= nums[i-1]
            products[len(products)-1-i] *= mult

            
        return products
    
    def productExceptSelf2(self, nums: list[int]) -> list[int]:
        prefix = [1]
        suffix = [1]
        products = [1] * len(nums) 
        mult = 1
        for i in range(1,len(nums)):
            prev_val = nums[i-1]
            mult *= prev_val
            prefix.append(mult)
        
        mult = 1
        nums.reverse()
        for i in range(1,len(nums)):
            prev_val = nums[i-1]
            mult *= prev_val
            suffix.append(mult)

        suffix.reverse()
        #print(prefix)
        #print(suffix)

        for i in range(len(products)):
            products[i] = prefix[i] * suffix[i]
        
        return products