class Solution:
    def grayCode(self, n: int) -> List[int]:
        def backtrack(n):
            if n==1:
                return [0,1]
            if n==0:
                return [0]
            prev = backtrack(n - 1)                
            add_on=1<<(n-1)
            new_codes = prev + [add_on | x for x in reversed(prev)]
            return new_codes

        return backtrack(n)

        return backtrack(n)

            
