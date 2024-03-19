class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        logarithm = math.log(n, 4)
        return logarithm == int(logarithm)