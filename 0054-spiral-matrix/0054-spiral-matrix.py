class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top,bottom=0,len(matrix)-1
        left,right=0,len(matrix[0])-1
        res=[]
        while top<=bottom and left<=right:
            for row in range(left,right+1):
                res.append(matrix[top][row])

            for col in range(top+1,bottom+1):
                res.append(matrix[col][right])
            
            if top<bottom:
                for row in range(right-1,left-1,-1):
                    res.append(matrix[bottom][row])
            
            if left < right:
                for row in range(bottom - 1, top, -1):
                    res.append(matrix[row][left])
            top+=1
            right-=1
            left+=1
            bottom-=1
        return res