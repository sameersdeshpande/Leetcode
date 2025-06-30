class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if n == 0: 
        #     return 1.0
        # if n < 0: 
        #     return 1.0 / self.myPow(x, -1 * n)
        # if n %2 ==1:
        #     return x * self.myPow(x * x, (n - 1) / 2)
        # else:
        #     return self.myPow(x * x, n / 2)
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

                    