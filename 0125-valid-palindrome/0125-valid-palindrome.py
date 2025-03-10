class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        set="".join(c.lower() for c in s if c.isalnum())
        left , right = 0 , len(set)-1

        while left<=right:
            if set[left]==set[right]:
                left+=1
                right-=1
            else:
                return False
        return True