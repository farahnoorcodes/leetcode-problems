class Solution:
    def addDigits(self,num):
        if num<=9:
            return num

        sum=0

        while num>0:
            sum+=num%10
            num=num//10
        return self.addDigits(sum)


