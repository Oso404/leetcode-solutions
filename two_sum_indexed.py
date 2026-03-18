"""

167. Two Sum II - Input Array Is Sorted
key takeaway: use two pointers to compare the sum of the two numbers and move ptrs accordingly
i think its simpler than regular 2sum because the array is sorted 

[2,3,6,6,9] 9
question is....
when do we increment left_ptr and right_ptr 
which do we increment

we can also use simple hashmap like regular 2sum
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left_ptr = 0
        right_ptr = len(numbers)-1
        while left_ptr < right_ptr:
            if numbers[right_ptr] + numbers[left_ptr] == target:
                left_ptr+=1
                right_ptr+=1
                return [left_ptr,right_ptr]
            elif numbers[right_ptr] + numbers[left_ptr] < target:
                left_ptr+=1
                continue
            else:
                right_ptr-=1
                continue
        return []



