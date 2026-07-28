class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output = {}

        for s in strs:
            word = "".join(sorted(s))
            if word in output:
                output[word].append(s)
            else:
                output[word] = [s]

        return list(output.values())

    

        