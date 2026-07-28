class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq_hash = {}
        l = 0
        best = 0

        for r, ch in enumerate(s):
            freq_hash[ch] = freq_hash.get(ch, 0) + 1
            most_freq = max(freq_hash.values())
            while (r - l + 1) - most_freq > k:
                freq_hash[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)

        return best
            

            



        
                
        
        