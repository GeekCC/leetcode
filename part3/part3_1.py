import sys
import queue


class TreeNode(object):
    def __init__(self, val, left = None, right = None):
        self.value = val
        self.left = left
        self.right = right

def balance(head):
    def search(head):
        if head == None:
            return 0
        left = search(head.left)+1
        right = search(head.right)+1
        if abs(left - right) > 1:
            return False
        return max(left,right) #返回左右最长的
    if search(head) == False:
        return False
    return  True

#层序遍历
def show_tree(head):
    que = queue.Queue()
    que.put(head)
    while que.empty()!= True:
        level_node_num = que.qsize()
        for i in range(level_node_num):
            temp = que.get()
            print(temp.value,end="  ")
            if temp.left != None:
                que.put(temp.left)
            if temp.right != None:
                que.put(temp.right)
        print()

if __name__ == "__main__":
    phead1 = TreeNode(1, TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(5,TreeNode(6)))
    phead2 = TreeNode(1,TreeNode(2,TreeNode(3,TreeNode(4))), TreeNode(5,TreeNode(6),TreeNode(7)))
    show_tree(phead2)
    print()
    show_tree(phead1)
    print(balance(phead1))
    print(balance(phead2))