
def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # # 方法一：将nums2数组添加到nums1数组的后面为0的部分
        # nums1[m:] = nums2
        # nums1.sort()


        # # 方法二：双指针正向比较，利用m+n的新数组存放比较后的结果
        # left_pointer = 0
        # right_pointer = 0
        # temp_arr = []

        # while (left_pointer<m or right_pointer<n):
        #     # case1：nums1数组已经比较完了，则将nums2数组的剩余部分插入合并后的数组
        #     if left_pointer == m:
        #         temp_arr.append(nums2[right_pointer])
        #         right_pointer += 1
        #     # case2：nums2数组比较完了，将nums1数组的剩余部分插入合并后数组
        #     elif right_pointer == n:
        #         temp_arr.append(nums1[left_pointer])
        #         left_pointer += 1
        #     # case3：nums1数组元素小于nums2数组元素，将nums1元素插入合并后的数组
        #     elif nums1[left_pointer] <= nums2[right_pointer]:
        #         temp_arr.append(nums1[left_pointer])
        #         left_pointer += 1
        #     # case4：nums2数组元素小于nums1数组元素，将nums2元素插入合并后的数组
        #     else:
        #         temp_arr.append(nums2[right_pointer])
        #         right_pointer += 1
        
        # nums1[:] = temp_arr



        # 方法三：逆序双指针，利用nums1数组从后往前可以直接覆盖的特点
        if m == 0:
            for i in range(len(nums1)):
                nums1[i] = nums2[i]
            return

        # 在nums1数组中从后向前倒着比较并插入元素

        insert_pointer = m + n - 1  # 合并后的数组的最后一位

        left_pointer = m - 1   # nums1数组的最后一位
        right_pointer = n - 1  # nums2数组的最后一位

        while (right_pointer>=0 or left_pointer >=0):
            if left_pointer == -1:
                nums1[insert_pointer] = nums2[right_pointer]
                right_pointer -= 1
            elif right_pointer == -1:
                nums1[insert_pointer] = nums1[left_pointer]
                left_pointer -= 1
            elif nums1[left_pointer] >= nums2[right_pointer]:
                nums1[insert_pointer] = nums1[left_pointer]
                left_pointer -= 1
            else:
                nums1[insert_pointer] = nums2[right_pointer]
                right_pointer -= 1

            # 每次循环在末尾插入元素后，指示插入位置的指针向前移动一位
            insert_pointer -= 1  


arr1 = [1,2,3,0,0,0]
m = 3
arr2 = [2,5,6]
n = 3

merge(arr1,m,arr2,n)
print(arr1)