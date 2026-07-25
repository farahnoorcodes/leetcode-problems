class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        sum1 = 0
        for i in nums:
            total += i          # element sum — every number counts here
            n = i
            while n > 9:
                rem = n % 10
                sum1 += rem
                n = n // 10
            sum1 += n            # add the last remaining digit
        return abs(total - sum1)
