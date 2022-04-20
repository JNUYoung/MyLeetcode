# 输入一个长度为n的整数数组height，每条线的端点为(i,height[i])，找出两个元素对应的
# 垂线与x轴围成的最大的面积


from sklearn.preprocessing import maxabs_scale


def maxArea(height):

    max_v = 0

    # for i in range(len(height)):
    #     for j in range(i+1, len(height)):
    #         temp = (j-i)*min(height[i], height[j])
    #         if temp >= max_v:
    #             max_v = temp

    # return max_v
    #
    #  面积的计算公式为(right-left)*min(height[left],height[right])
    #  使用暴力方法时，就是通过两重循环，计算并更新最大的面积
    #  这是一种正向的推理思维的过程，但是存在许多不必要的计算过程


    """
        第二种方法，使用双指针的方法：
            容纳最多的水，或者说最大的面积，主要就是确定两个端点。
            因此，使用两个指针来模拟所有可能的端点对（left，right）

        关键是更新指针时，是移动更小值的指针，还是移动更大值的指针？
            答案是：移动更小值的指针
    """
    left = 0
    right = len(height)-1

    while left<right:
        temp = (right-left) * min(height[left],height[right])
        if temp >= max_v:
            max_v = temp
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        else:
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        
    return max_v


test = [1,8,6,2,5,4,8,3,7]
print(maxArea(test))
