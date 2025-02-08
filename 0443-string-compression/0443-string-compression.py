class Solution:
    def compress(self, chars: List[str]) -> int:
        w=0
        r=0

        while r<len(chars):
            char = chars[r]
            c=0

            while r<len(chars) and chars[r]==char:
                c+=1
                r+=1
            
            chars[w]=char
            w+=1

            if c>1:
                for digit in str(c):
                    chars[w]=str(digit)
                    w+=1
        return w