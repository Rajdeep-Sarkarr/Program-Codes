import random
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]

    def reset(self) -> List[int]:
        return self.original[:]

    def shuffle(self) -> List[int]:
        ar = self.original[:]
        n = len(ar)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            ar[i], ar[j] = ar[j], ar[i]
        return ar

# Example usage:
nums = [1, 2, 3]
obj = Solution(nums)

print("Reset:", obj.reset())
print("Shuffle:", obj.shuffle())
print("Shuffle again:", obj.shuffle())
