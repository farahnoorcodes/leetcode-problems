class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        val=0
        original=num
        while num>0:
            rem=num%10
            if original%rem==0:
                val+=1
            num=num//10
        return val