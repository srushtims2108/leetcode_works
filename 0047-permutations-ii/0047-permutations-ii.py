class Solution:
    def permuteUnique(self, nums):
        res = []
        nums.sort()

        def backtrack(path,remaining):
            if len(path) == len(nums):
                res.append(path)
                return
            used = set() 
            for i in range(len(remaining)):
                if remaining[i] in used:
                    continue  
                used.add(remaining[i])
                backtrack(path+[remaining[i]],remaining[:i]+remaining[i+1:])
        backtrack([],nums)
        return res
