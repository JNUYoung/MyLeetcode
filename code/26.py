class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        left = 1
        right = 1
        # left指针和right指针从第二个元素开始，这是一个关键的地方
        # 让右指针移动的同时，判断其所指元素和上一个元素是否相等，因为数组是升序排列
        # 因此出现连续两个元素不相等时，将右指针覆盖到左指针，再移动左指针；
        # 若元素一直连续相等，则移动右指针到不等元素 

        while right<length:
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left = left + 1
            right = right + 1 
        return left