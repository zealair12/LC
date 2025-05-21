class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        pairs = 0
        dictRow = {}
        dictCol = {}
        n = len(grid)

        for row in range(n):
            dictRow[row] = grid[row]
            dictCol[row] = []

        for c in range(n):
            for r in range(n):
                dictCol[c].append(grid[r][c])
        
        for rows in dictRow:
            for cols in dictCol:
                if dictRow[rows] == dictCol[cols]:
                    pairs += 1
        
        return pairs
            