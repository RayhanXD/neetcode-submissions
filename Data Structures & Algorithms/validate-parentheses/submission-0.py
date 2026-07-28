class Solution:
    def isValid(self, s: str) -> bool:

        if (len(s) % 2 != 0):
            return False

        s_stack = []
        opening = ["(", "[", "{"]
        closing = [")", "]", "}"]

        for char in s:
            if char in opening:
                s_stack.append(char)
            else:
                if len(s_stack) == 0:
                    return False
                else:
                    if opening.index(s_stack.pop()) != closing.index(char):
                        return False

        return len(s_stack) == 0
            