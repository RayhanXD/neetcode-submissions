class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_hash = {}
        t_hash = {}

        if len(s) == len(t):
            for letter in s:
                if letter not in s_hash:
                    s_hash[letter] = 1
                else:
                    s_hash[letter] += 1
            for letter in t:
                if letter not in t_hash:
                    t_hash[letter] = 1
                else:
                    t_hash[letter] += 1
        else:
            return False

        return s_hash == t_hash
