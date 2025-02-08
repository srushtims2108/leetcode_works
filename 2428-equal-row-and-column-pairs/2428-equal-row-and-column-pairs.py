class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n=len(grid)
        c=0
        m_x=0
        for i in range(n):
            for j in range(n):
                    if grid[i]==[grid[k][j] for k in range(n)]:
                        c+=1
         
        return c