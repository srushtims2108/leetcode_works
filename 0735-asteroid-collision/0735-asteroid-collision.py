class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]

        for i in asteroids:
            while stack and stack[-1]>0 and i<0:
                prev = stack.pop()
                if abs(i)<prev:
                    stack.append(prev)
                    break
                elif abs(i)==prev:
                    break
            else:
                stack.append(i)
        
        return stack   