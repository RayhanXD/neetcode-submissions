class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        r = 1
        best = 1
        counter = 1

        if s == "":
            return 0

        storage = {s[l]}

        while (r < len(s)):
            if s[r] not in storage:
                storage.add(s[r])
                r += 1
                counter += 1
                best = max(best, counter)

            else:
                storage.remove(s[l])
                l += 1
                counter -= 1

        return best



        