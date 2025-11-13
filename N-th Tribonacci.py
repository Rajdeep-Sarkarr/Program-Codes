class Solution:
    def tribonacci(self, n: int) -> int:
        F = [0, 1, 1] + [0] * 35
        if n < 3:
            return F[n]
        else:
            for i in range(3, n + 1):
                F[i] = F[i - 1] + F[i - 2] + F[i - 3]
        return F[n]


# Example usage
obj = Solution()
print(obj.tribonacci(4))
print(obj.tribonacci(25))
print(obj.tribonacci(0))
