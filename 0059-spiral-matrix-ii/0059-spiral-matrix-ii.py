class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top,bottom=0,n-1
        left,right=0,n-1
        matrix = [[0] * n for _ in range(n)]
        count=1
        while top<=bottom and left<=right:

            for row in range(left,right+1):
                matrix[top][row]=count
                count+=1
            top+=1
            for col in range(top,bottom+1):
                matrix[col][right]=count
                count+=1
            right-=1
            if top<=bottom:
                for row in range(right,left-1,-1):
                    matrix[bottom][row]=count
                    count+=1
                bottom-=1
            if left<=right:
                for col in range(bottom,top-1,-1):
                    matrix[col][left]=count
                    count+=1
                left+=1

        return matrix
            