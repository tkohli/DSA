class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        The main problem with this question is to keep negative number tracks 
        and then also the int range in python as it uses dynamic memory allocation
        Trying to do a clear implementation to  ake this easy 
        For example, we divide(5000, 14):

        After the first inner loop: the_sum = 3584 which is 14 multiplied 256 times.
        We can't multiply any more — because after 256 is coming 256 + 256 = 512 and 14 * 512 = 7168 which is larger than our dividend, so we exit the inner loop,
        Reducing dividend: dividend = 5000 - 3584 = 1416
        And moving to another cycle of outer loop
        After the second inner loop: the_sum = 896 which is 14 multiplied 64 times.
        Third: the_sum = 448 which is 14 multiplied 32 times.
        And so on
        Finally we have: quotient = 256 + 64 + 32 + 4 + 1 = 357 
        """
        negative = (dividend < 0) != (divisor < 0)  # perform XOR
        dividend = abs(dividend)
        divisor = abs(divisor)
        theSum = divisor
        quotient = 0
        while theSum <= dividend:
            currentquotient = 1
            while theSum*2 <= dividend:
                theSum *= 2
                currentquotient += currentquotient
            dividend -= theSum
            theSum = divisor
            quotent += currentquotient
        return min(2147483647, max(quotient if negative else quotient, -2147483648))
