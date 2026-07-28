class Solution:

    def encode(self, strs: List[str]) -> str:

        for i, word in enumerate(strs):
            length = len(word)
            strs[i] = str(length) + "#" + word

        result = ""

        for word in strs:
            result = result + word

        return result


    def decode(self, s: str) -> List[str]:

        words = []

        i = 0
        while i < len(s):
            hash_index = s.find("#", i)
            length = int(s[i: hash_index])
            word = s[hash_index + 1: hash_index + length + 1]
            words.append(word)
            i = hash_index + length + 1
                
        return words

