# 1015. Smallest Integer Divisible by K

LeetCode: https://leetcode.com/problems/smallest-integer-divisible-by-k/

## Problem
Given a positive integer k, return the length of the smallest positive integer n consisting only of the digit 1 (in decimal) such that n is divisible by k. If no such n exists, return -1.

## Approach
Build the number of repeated 1s incrementally while keeping only its remainder modulo k to avoid large integers.

- If k is divisible by 2 or 5, return -1 (no such number exists).
- Maintain rem = (rem * 10 + 1) % k for each added digit.
- If rem becomes 0, the current length is the answer.
- By the pigeonhole principle, checking up to k steps is sufficient.

## Solution (Python)

```python
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        rem = 0
        for length in range(1, k + 1):
            rem = (rem * 10 + 1) % k
            if rem == 0:
                return length
        return -1
```

## Complexity
- Time: O(k)
- Space: O(1)

## Example

```python
if __name__ == "__main__":
    sol = Solution()
    print(sol.smallestRepunitDivByK(3))  # 3
    print(sol.smallestRepunitDivByK(7))  # 6
    print(sol.smallestRepunitDivByK(2))  # -1
```

## Author
- srushtims2108