class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        t_gas=sum(gas)
        t_cost=sum(cost)

        if t_gas<t_cost:
            return -1
        start_index=0
        tank=0

        for i in range(len(gas)):
            
            tank+=gas[i]-cost[i]
            if tank<0:
                tank=0
                start_index=i+1
    
        return start_index