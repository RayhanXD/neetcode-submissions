class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {"(": ")", "[": ']', "{": "}"}

        if len(s) % 2 != 0:
            return False

        stack = []

        for c in s:
            if c in pairs:
                stack.append(c)
            else:
                if not stack or pairs[stack.pop()] != c:
                    return False

        return not stack

            


        
            