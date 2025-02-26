###########################################################################
# 先序序列化反序列化
# 宽度序列化反序列化
#
# https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/
###########################################################################


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#---------------------------------------------------------------------------------   
#先序序列化反序列化
class Codec1:

    def serialize(self, root):
        return self.f(root)

    def f(self, root):
        if not root:
            return "#,"
        else:
            s = str(root.val) + ","
            return s + self.f(root.left) + self.f(root.right)

    def deserialize(self, data):
        lst = data.split(",")
        return self.g(lst)
    
    def g(self,lst):
        if len(lst) == 0: 
            return 
        x = lst.pop(0)
        if x == "#":
            return None
        head = TreeNode(x) 
        head.left = self.g(lst)
        head.right = self.g(lst)
        return head
    

#---------------------------------------------------------------------------------   
# 宽度序列化反序列化

class Codec2:

    def serialize(self, root):
        return self.f(root)

    def f(self, root):
        if not root:
            return "#,"

        s = str(root.val) + ","
        queue = [root]
        while queue:
            curNode = queue.pop(0)
            if curNode.left:
                queue.append(curNode.left)
                s += (str(curNode.left.val) + ",")
            else:
                s += "#,"
            if curNode.right:
                queue.append(curNode.right)
                s += (str(curNode.right.val) + ",")
            else:
                s += "#,"
        return s

    def deserialize(self, data):
        lst = data.split(",")
        return self.g(lst)
    
    def g(self,lst):
        x = lst.pop(0)
        if x == "#":
            return None
        head = TreeNode(x)
        queue = [head]
        while queue:
            curNode = queue.pop(0)
            curNode.left = self.generateNode(lst.pop(0)) 
            curNode.right = self.generateNode(lst.pop(0)) 
            if curNode.left:
                queue.append(curNode.left )
            if curNode.right:
                queue.append(curNode.right)
        return head

    def generateNode(self, val):
        if val == "#":
            return None
        return TreeNode(val)
    
#---------------------------------------------------------------------------------   


def main():
    s = "1,2,3,#,#,4,5,#,#,#,#"
    head = Codec2().deserialize(s)
    s = Codec2().serialize(head)
    print(s)





if __name__ == "__main__":
    main()