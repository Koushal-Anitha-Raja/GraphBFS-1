TC:0(n)
Sc:0(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        #creating a empty queue
        q=deque()
        q.append(root)
        
        #iteratting the root value
        while q:
            #finding the size of the queue to check at each level
            size=len(q)
            #to remove duplicates we are using hashset
            level= set()
            
            for i in range(size):
            #deleting from queue to add to node
                node=q.popleft()
            #adding the node val to each level
                level.add(node.val)
                #checking if it is a sibling or not 
                if node.left and node.right and ((node.left.val==x and node.right.val==y) or (node.left.val==y and node.right.val==x)):
                    #if it is sibling return false
                    return False
                #if the node is present append it to queue
                if node.left:
                    q.append(node.left)
                    #if the node is present append it to queue
                if node.right:
                    q.append(node.right)
                    #if both the x and y are at same level
            if x in level and y in level:
                #then return true
                return True
                #or return false
        return False
                
                
                                                
        