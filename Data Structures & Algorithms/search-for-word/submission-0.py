class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        past = set()

        def backtrack(r, c, i):

            if i == len(word):
                return True
            elif r >= len(board) or c >= len(board[0]) or r < 0 or c < 0:
                return False
            elif word[i] != board[r][c]:
                return False
            elif (r, c) in past:
                return False
            
            past.add((r, c))
            found = backtrack(r + 1, c, i + 1) or backtrack(r - 1, c, i + 1) or backtrack(r, c + 1, i + 1) or backtrack(r, c - 1, i + 1)
            past.remove((r, c))
            return found

        for i in range(len(board)):
            for j in range(len(board[i])):
                if backtrack(i, j, 0):
                    return True

        return False