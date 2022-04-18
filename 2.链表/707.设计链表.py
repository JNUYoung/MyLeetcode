# 链表中的节点表示
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None



class MyLinkedList(object):

    def __init__(self):
        self._head = Node(0)    # _head 表示初始化的链表的虚拟的头节点
        self._count = 0         # _count 表示当前链表中的节点的数目，除掉虚拟头节点，因此，初始为0

    def get(self, index):
        """
        获取第index个节点的值，如果索引无效，则返回-1
        :type index: int
        :rtype: int
        """
        if 0 <= index <= self._count:   # 如果index有效
            node = self._head
            for _ in range(index + 1):   # index = 0
                node = node.next
            return node.val
        else:
            return -1



    def addAtHead(self, val):
        """
        在第一个节点之前添加一个值为val的节点，该节点为链表的新的头节点
        :type val: int
        :rtype: None
        """
        temp = self._head.next
        self._head.next = Node(val)
        Node(val).next = temp



    def addAtTail(self, val):
        """
        将值为val的节点添加到链表的尾节点之后
        :type val: int
        :rtype: None
        """
        new_node = Node(val=val)    # 待添加的节点
        pointer = self._head        # 定义一个遍历用的指针
        while (pointer.next!=None): # 遍历到最后一个节点
            pointer = pointer.next
        pointer.next = new_node     # 最后一个节点指向新加入的节点


    # addAtHead 和 addAtTail 都是 addAtIndex的特殊情况
    def addAtIndex(self, index, val):
        """
        在链表中的第 index 个节点之前添加值为 val  的节点。
        如果 index 等于链表的长度，则该节点将附加到链表的末尾。
        如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0:
            index = 0
        elif index > self._count:
            return
        
        self._count += 1
        new_node = Node(val=val)
        previous_node,current_node = None,self._head   # 预先定义遍历的节点，因为要在index之前插入，因此让current_node最终指向index位置的节点
        for _ in range(index+1):
            previous_node,current_node = current_node,current_node.next   # 两个指针不断后移

        else:
            previous_node.next, new_node.next = new_node, current_node


    def deleteAtIndex(self, index):
        """
        如果索引index有效，则删除链表中的第index个节点
        :type index: int
        :rtype: None
        """
        if 0<= index <=self._count:

            self._count -= 1
            prev,pointer = None,self._head

            for _ in range(index+1):
                prev = pointer
                pointer = pointer.next
            
            prev.next = pointer.next
            
