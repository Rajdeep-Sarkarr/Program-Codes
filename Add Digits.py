class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return num
        elif num % 9 == 0:
            return 9
        else:
            return num % 9


# Example usage
obj = Solution()
print(obj.addDigits(38))
print(obj.addDigits(0))
print(obj.addDigits(99))
