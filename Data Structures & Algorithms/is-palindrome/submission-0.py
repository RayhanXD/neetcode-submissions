class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_s = []
        s = s.lower()
        for char in s:
            if char.isalnum():
                new_s.append(char)

        s = new_s
        l = 0
        r = len(s) - 1

        while(l <= r):
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True