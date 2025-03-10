class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        partitions = 0

        for char in s:
            if char in seen:
                partitions += 1
                seen.clear()
            seen.add(char)

        return partitions + 1

                

        