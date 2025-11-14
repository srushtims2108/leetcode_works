class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest=float('inf')

        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1

            while k>j:
                curr_sum=nums[i]+nums[j]+nums[k]
                if curr_sum==target:
                    return curr_sum
                if abs(curr_sum-target)<abs(closest-target):
                    closest=curr_sum

                if curr_sum<target:
                    j+=1
                else:
                    k-=1
                
        return closest

