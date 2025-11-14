class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        nums=[]
        for i in range(1,n+1):
            nums.append(i)
        for combo in combinations(nums, k):
            print(res.append(combo))
        return res