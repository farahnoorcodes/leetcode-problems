class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for i in range(len(words)):
            rev = words[i][::-1]
            if rev == words[i]:
                return words[i]
        return ""