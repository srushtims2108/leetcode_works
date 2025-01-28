class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output=[]
        max_candy = max(candies)

        for candy in candies:
            output.append(bool(candy+extraCandies>=max_candy))
        
        return output



        