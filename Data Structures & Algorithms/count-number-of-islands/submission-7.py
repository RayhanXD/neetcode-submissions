class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        past = set()

        def dfs(r, c):

            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0:
                return False
            elif grid[r][c] == "0":
                return False
            elif (r, c) in past:
                return False

            past.add((r, c))
            dfs(r + 1, c)
            dfs(r, c + 1)
            dfs(r - 1, c)
            dfs(r, c - 1)
            return 

        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in past:
                    dfs(i, j)
                    islands += 1

        return islands

        