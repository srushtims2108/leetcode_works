class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        prev=self.countAndSay(n-1)
        return self.generate(prev)

    def generate(self,s):
        i=0
        ans=[]
        n=len(s)
        while i<n:
            count=1
            while i+1<n and s[i]==s[i+1]:
                count+=1
                i+=1
            ans.append(str(count)+s[i])
            i+=1
        return "".join(ans)
            