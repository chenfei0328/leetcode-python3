class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if not gas or not cost:
            return -1
        
        remain, lack, index = 0, 0, 0
        for i, g in enumerate(gas):
            remain += g - cost[i]
            if remain < 0:
                index = i + 1
                lack += remain
                remain = 0
                
        return index if remain + lack >= 0 else -1