import sys
import queue


class TreeNode(object):
    def __init__(self, val, left = None, right = None):
        self.value = val
        self.left = left
        self.right = right


#层序遍历即可， 该节点所在层数即为到根节点距离
def show_tree(head):
    que = queue.Queue()
    que.put(head)
    level = 0
    length_sum = 0
    while que.empty()!= True:
        level_node_num = que.qsize()
        for i in range(level_node_num):
            temp = que.get()
            length_sum += temp.value*level
            print(temp.value,end="  ")
            if temp.left != None:
                que.put(temp.left)
            if temp.right != None:
                que.put(temp.right)
        print()
        level += 1
    print("带权路径长度：", length_sum)

if __name__ == "__main__":
    phead1 = TreeNode(1, TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(5,TreeNode(6)))
    phead2 = TreeNode(1,TreeNode(2,TreeNode(3,TreeNode(4))), TreeNode(5,TreeNode(6),TreeNode(7)))
    show_tree(phead2)
    print()
    show_tree(phead1)
