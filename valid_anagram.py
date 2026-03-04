class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm1 = dict()
        hm2 = dict()
        for i in range(len(s)):
            if s[i] not in hm1:
                hm1[s[i]] = 1
            else:
                hm1[s[i]] += 1
            if t[i] not in hm2:
                hm2[t[i]] = 1
            else:
                hm2[t[i]] += 1
        return hm1 == hm2

        