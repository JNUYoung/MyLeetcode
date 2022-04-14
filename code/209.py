# leetcode 209  长度最小的子数组
# middle

# description:
# 给定一个含有n个正整数的数组和一个正整数target，找出数组中满足和大于等于target的长度最小的连续子数组，返回该子数组长度，若不存在，返回0；


from numpy import Infinity


def minSubArrayLen(target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        result = Infinity
        # if not exist

        for i in range(0,len(nums)):
            temp_sum = 0
            for j in range(i,len(nums)):
                temp_sum += nums[j]
                if (temp_sum >= target):
                    subArrayLen = j - i + 1
                    result = subArrayLen if subArrayLen < result else result
                    break
        
        if result < Infinity:
            return result
        else:
            return 0
        

                


input = [1,1,1]

print(minSubArrayLen(11,input))