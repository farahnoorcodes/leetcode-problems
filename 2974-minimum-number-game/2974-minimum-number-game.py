class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums.sort()
        arr = []
        for i in range(0, len(nums), 2):
            arr.append(nums[i + 1])  # Bob's (larger) goes first
            arr.append(nums[i])      # Alice's (smaller) goes second
        return arr
        