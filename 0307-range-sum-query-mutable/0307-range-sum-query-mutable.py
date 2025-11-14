class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums[:]                 # store original array
        self.bit = [0] * (self.n + 1)       # Fenwick Tree array

        # build BIT with initial values
        for i, num in enumerate(nums):
            self._add(i + 1, num)

    def _add(self, i: int, delta: int) -> None:
        """Helper: add delta to index i in Fenwick Tree"""
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def update(self, index: int, val: int) -> None:
        """Update nums[index] to val"""
        diff = val - self.nums[index]
        self.nums[index] = val
        self._add(index + 1, diff)

    def _prefix_sum(self, i: int) -> int:
        """Helper: prefix sum from 1..i"""
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def sumRange(self, left: int, right: int) -> int:
        """Return sum between left and right inclusive"""
        return self._prefix_sum(right + 1) - self._prefix_sum(left)