class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()
        c=0
        init=arr[0]
        ans=[]
        for i in arr:
            if i==init:
                c+=1
            elif i!=init:
                ans.append(c)
                init=i
                c=1
        ans.append(c)
        return len(set(ans))==len(ans)