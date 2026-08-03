class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        already_contained_numbers = []
        while n != 1:
            if n in already_contained_numbers:
                return False
            already_contained_numbers.append(n)
            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n = n // 10
            n = total
        return True