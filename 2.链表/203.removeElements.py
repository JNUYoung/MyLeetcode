"""
    迭代的方法：
        
"""



# 单链表节点的定义

from curses import noecho
from typing import List


class ListNode(object):
    def __init__(self,val,next):
        """
            val : int / float
            next : ListNode
        """
        self.val = val
        self.next = next


# 从单链表中移除指定的节点元素

def removeNodes(head,val):
    """
        head : ListNode
        val : 待删除的目标值
    """

    # 思路：遍历每一个节点，若节点的值等于指定值，则删除该节点
    # 为方便遍历和删除操作，使得头节点和其它节点都能够按照同样的方式进行
    # 增加一个虚拟的头节点

    virtual_head = ListNode(val=0,next=head)  # 虚拟头节点，指向链表中真实的头节点
    
    my_pointer = virtual_head    # 定义一个遍历指针，从虚拟头节点开始进行遍历

    # 依次判断指针所指向的后一个元素的值是否是给定值
    while (my_pointer.next != None):     # 遍历终点为最后一个节点
        if my_pointer.next.val == val:
            my_pointer.next = my_pointer.next.next
        else:
            my_pointer = my_pointer.next  # 指针后移
    
    return virtual_head.next    # 返回虚拟头指针的后一个节点，即第一个真实节点