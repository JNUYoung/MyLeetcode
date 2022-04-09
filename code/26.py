def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        left = 0
        right = 0

        if length == 0:
            return 0 
        if length == 1:
            return 1
        if length == 2:
            return 1 if nums[0] == nums[-1] else 2

        while right<length:
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left = left + 1
            right = right + 1 
        return left

print(removeDuplicates([1,1]))