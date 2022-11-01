#Time_Complexity: O(n)
#Space_Complexity: O(n)

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #the length of any given word
        m = len(wordList[0])
        #use set to re,ove the duplicates
        wordList = set(wordList)    
        #add the beginWord into the wordList
        wordList.add(beginWord) 
        
        # adjacency matrix to the pair value
        adj = defaultdict(list)
        
        #iterate through the wordlist
        for word in wordList:  
            for i in range(m): 
                #slice the word at each stage
                s = word[:i]+ "_" +word[i+1:]  
                #Append the  word into the adjacency matrix
                adj[s].append(word) 
        
        
        #q using deque
        q = deque() 
        #Append the beignWord to the queue
        q.append(beginWord)
        #Initialize visited set
        visited = set() 
        dist = 0   
         #Add the beginWord into the visited set
        visited.add(beginWord)
        
        #until the queue is empty
        while q:   
            #the size parameter for each level by  level traversal
            dist+=1 
            size = len(q)   
            
            for _ in range(size): 
                 #Pop the first element in the q and store it in curr
                curr = q.popleft() 
                for i in range(m):  
                     #add the  special character "_" at eveery index
                    s = curr[:i]+ "_" +curr[i+1:]   
                    #For the words in adj
                    for nextWord in adj[s]:  
                        #if it is not in visited set
                        if nextWord not in visited:
                            #then add it to visited set
                            visited.add(nextWord)
                            q.append(nextWord)
                            #If the nextWord is equal to endWord return dist+1
                            if nextWord == endWord: 
                                return dist+1
        #If nothing is found return 0                    
        return 0    
