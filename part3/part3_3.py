import sys
import queue
class TreeNode(object):
    def __init__(self, val, left = None, right = None):
        self.value = val
        self.left = left
        self.right = right

maxlen = 0
#深度优先遍历
def dfs(phead):
    global maxlen
    if phead == None:
        return 0
    left = dfs(phead.left)
    right = dfs(phead.right)
    if maxlen < left + right:
        maxlen = left + right
    return left+1 if left > right else right+1
    
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
    show_tree(phead1)
    dfs(phead1)
    print("banjing:", maxlen)
    show_tree(phead2)
    dfs(phead2)
    print("banjing:", maxlen)
