import sys
import queue
class TreeNode(object):
    def __init__(self, val, left = None, right = None):
        self.value = val
        self.left = left
        self.right = right

maxsum = 0
maxhead = TreeNode(0)
#深度优先遍历
def dfs(phead):
    global maxsum
    global maxhead
    if phead == None:
        return phead, 0
    left, leftvalue= dfs(phead.left)
    right, rightvalue= dfs(phead.right)
    subsum = leftvalue + rightvalue + phead.value
    if maxsum < subsum:
        maxsum = subsum
        maxhead = phead
    return phead, subsum

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
    phead1 = TreeNode(-4, TreeNode(-2, TreeNode(11, TreeNode(-3),TreeNode(1))), TreeNode(3, TreeNode(2), TreeNode(-5, None, TreeNode(4))))
    phead2 = TreeNode(1,TreeNode(2,TreeNode(3,TreeNode(4))), TreeNode(5,TreeNode(6),TreeNode(7)))
    show_tree(phead1)
    dfs(phead1)
    show_tree(maxhead)
    print("zishu:", maxsum)
    show_tree(phead2)
    dfs(phead2)
    show_tree(maxhead)
    print("zishu:", maxsum)