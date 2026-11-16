from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        freq_s = Counter(s)
        least_freq_char = ""

        for char, freq in freq_s.items():

            if freq == 1:
                least_freq_char = char
                break

        for i, c in enumerate(s):
            if least_freq_char == c:
                return i
 
        return -1
        