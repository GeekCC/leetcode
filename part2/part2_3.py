import sys

data = [1,2,3,4,5,6,7,8,9]

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

#使用快慢指针，将链表分为两半，将后一半反转，然后依次重新组合
def rearrange(phead):
    p_slow = phead
    p_fast = phead.next
    while p_fast != None and p_fast.next != None:
        p_slow = p_slow.next
        p_fast = p_fast.next.next
    phead1 = phead
    phead2 = p_slow.next
    p_slow.next = None
    return merge(phead1, reverse(phead2))

#反转链表
def reverse(phead):
    ppre = None
    p = phead
    pnext = phead.next
    while pnext != None:
        p.next = ppre
        ppre = p
        p = pnext
        pnext = pnext.next
    p.next = ppre
    return p

#把2 合并到 1 中（2需比1短）
def merge(phead1, phead2):
    p1 = ptemp1 = phead1
    p2 = ptemp2 = phead2
    while p2 != None:
        ptemp2 = p2.next
        p2.next = p1.next
        p1.next = p2
        p1 = p1.next.next
        p2 = ptemp2
    return ptemp1

#输出链表内容
def listNode(phead):
    p = phead
    while p != None:
        print(p.val)
        p = p.next

if __name__ == "__main__":
    #创建链表
    head = Node(data[0]) #存储头节点
    p = head    #临时指针用来创建list ， 此处利用python浅拷贝 ，p和head共享一个内存的变量
    for i in data[1:]:
        node = Node(i)
        p.next = node
        p = p.next
    listNode(rearrange(head))

    



