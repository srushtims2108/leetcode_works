class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
    
        word1=sorted(word1)
        word2=sorted(word2)
        s1,s2=[],[]
        if len(word1)!=len(word2):
            return False
        if set(word1) != set(word2):
            return False

        init=word1[0]
        c=0
        for i in word1:

            if i==init:
                c+=1
            else:
                s1.append(c)
                c=1
                init=i
        s1.append(c)

        init=word2[0]
        c=0
        for i in word2:
        
            if i==init:
                c+=1
            else:
                s2.append(c)
                c=1
                init=i
        s2.append(c)
        
        return sorted(s1)==sorted(s2)