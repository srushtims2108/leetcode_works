class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = max(len(word1), len(word2))
        answer=[]
        answer1=[]
        for  i in range(word):
            if i<len(word1):
               answer.append(word1[i]) 
            if i<len(word2):
                answer.append(word2[i])
        return ''.join(answer)