class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2!=str2+str1:
         return ''

        min_length = min(len(str1),len(str2))

        for i in range(min_length , 0 , -1):
            str=str1[:i]
            if len(str1)%i==0 and len(str2)%i==0:
             return str

