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
            
        


