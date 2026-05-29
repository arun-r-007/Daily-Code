class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []

        for i in nums:
            a = sum(int(d) for d in str(i))
            result.append(a)

        return min(result)