"""
125. Valid Palindrome
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

key takeaway: use two pointers to compare chars from start and end and move towards center (double pointer technique)
we continue even if current char is not alphanumeric because the next char might not also be alphanumeric as well!
"""




class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_ptr = 0
        right_ptr = len(s)-1
        while left_ptr < right_ptr:
            if not s[left_ptr].isalnum():
                left_ptr+=1
                continue
            
            if not s[right_ptr].isalnum():
                right_ptr-=1
                continue
            
            if s[left_ptr].lower() != s[right_ptr].lower():
                print(s[left_ptr],s[right_ptr])
                return False
            
            print(s[left_ptr],s[right_ptr])
            
            left_ptr+=1
            right_ptr-=1
        return True
            
            
            
