class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        frequency_dict = {}
        for i in s:
            frequency_dict[i] = frequency_dict.get(i, 0) + 1
        for j in t:
            if j not in frequency_dict:
                return False
            elif j in frequency_dict and frequency_dict.get(j,0) == 0:
                return False
            elif j in frequency_dict:
                frequency_dict[j] -= 1
        return True