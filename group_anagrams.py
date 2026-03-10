"""
49. Group Anagrams
given an array of strings, group anagrams together.

key takeaway: use a unique identifier for each group of anagrams, in this case the count for each letter 
use of alphabet allows us to use a fixed size array of 26, and we can convert the count string as a key for the group 

"""
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group_numbers = dict() 
        group_anagrams = []
        for word in strs:
            starter = ['0'] * 26 
            for letter in word:
                index = ord(letter) - ord('a')
                starter[index] = str(int(starter[index]) + 1) 
            combined = '#'.join(starter)
            if combined not in group_numbers:
                group_numbers[combined] = len(group_anagrams)
                group_anagrams.append([word])
            else:
                group_anagrams[group_numbers[combined]].append(word)
        return group_anagrams
            
        


