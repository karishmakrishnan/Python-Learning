

class Solution:
    def addDigits(self, num: int) -> int:
        sum = 0;
        while(num%10 != 0):
            rem = num % 10
            num = num//10
            sum += rem
        return sum