#TC:0(n)+3n
#Sc:3n+n

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        adj=defaultdict(list)
        q=deque()
        #adding the root value to queue
        q.append(root)
        visited=set()
        #iterate until the queue is there
        while q:
            curr=q.popleft()
            #until the curren left is there
            if curr.left:
                #add the parent to the left child 
                adj[curr.left].append(curr)
                #add the parent to the curr element 
                adj[curr].append(curr.left)
                #adding the node to queue
                q.append(curr.left)
            
            if curr.right: 
                #add the parent to the right child 
                adj[curr.right].append(curr)
                #add the parent to the curr element 
                adj[curr].append(curr.right)
                #adding the node to queue
                q.append(curr.right)  
                
            
        #add target to the queue to reduce by one
        q.append(target)
        #until the queue is empty and k is not zero
        while q and k>0:
            size =len(q)
            #size arameter for each level  
            for _ in range(size):
                currNode=q.popleft()
                visited.add(currNode)
                #for every neighbour in the adj matrix
                for neigh in adj[currNode]:
                    if neigh not in visited:
                    #append it to the queue
                        q.append(neigh)
                    
                    
    #reduce the target value one at each state
            k-=1
        result=[]
        #for the iteration in queue
        for node in q:
            #appending the queue value to it
            result.append(node.val)
            #return teh result
        return result
        
        
        
