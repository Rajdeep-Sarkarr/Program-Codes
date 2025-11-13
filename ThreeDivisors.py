class Solution:
    def isThree(self, n: int) -> bool:
        if n == 1:
            return False
        c = 0
        for i in range(1, n + 1):
            if n % i == 0:
                c += 1
        return c == 3


# Example usage
obj = Solution()
print(obj.isThree(4))
print(obj.isThree(16))
print(obj.isThree(1))
