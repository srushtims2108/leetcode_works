class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]
        i=0
        j=0
        if len(nums)==1:
            res.append(f"{nums[i]}")
            return res
        while i<len(nums)-1:
            if nums[i]+1==nums[i+1]:
                i+=1
                if i==len(nums)-1:
                    res.append(f"{nums[j]}->{nums[i]}")
            else:
                if i!=j:
                    res.append(f"{nums[j]}->{nums[i]}")
                else:
                    res.append(f"{nums[i]}")
                i+=1
                j=i
            if i==len(nums)-1 and nums[i]-1!=nums[i-1]:
                res.append(f"{nums[i]}")
            
        return res            