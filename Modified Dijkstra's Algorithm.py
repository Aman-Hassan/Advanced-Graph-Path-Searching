class MaxHeap:
    class Node:
        def __init__(self,key,parent=None,r_child=None,l_child=None) -> None:
            self._k = key    #2 tuple of the form (v,c) where v is the vertex number and c is the capacity
            self._p = parent #parent of present node
            self._rc = r_child #right child
            self._lc = l_child #left child

    def __init__(self):   #L contains the list of values
        self._heap = []  #This is list of pointers according to our required heap structure
        self._pointerlist= [1] #This is list of pointers according to index i
        self._n = 0  #no of nodes = 0 initially
        self._root = None #root of heap 
        self._tail = None #last element of heap
        
    
    def isempty(self):
        if (self.n == 0):
            return(True)
        else:
            return (False)
    
    def heapup(self,u):
        u1 = u
        
        if u1._p == None:
            return()

        while u1._p._k[1] <= u1._k[1]:
            if u1._p._k[1] == u1._k[1] and u1._p._k[0] < u1._k[0]:
                i1 = u1._k[0]
                i2 = u1._p._k[0]
                u1._p._k,u1._k= u1._k,u1._p._k
                self._pointerlist[i1+1],self._pointerlist[i2+1] = self._pointerlist[i2+1],self._pointerlist[i1+1]
                u1 = u1._p
            elif u1._p._k[1] == u1._k[1] and u1._p._k[0] > u1._k[0]:
                break
            else:
                i1 = u1._k[0]
                i2 = u1._p._k[0]
                u1._p._k,u1._k= u1._k,u1._p._k
                self._pointerlist[i1+1],self._pointerlist[i2+1] = self._pointerlist[i2+1],self._pointerlist[i1+1]
                u1 = u1._p
            if u1._p == None:
                break
        return()

    def heapdown(self,u):
        u1 = u
        v = None

        if u1._rc == None and u1._lc != None:
                v = u1._lc
                if v._k[1] > u1._k[1]:
                    i1 = u1._k[0]
                    i2 = v._k[0]
                    v._k,u1._k= u1._k,v._k
                    self._pointerlist[i1+1],self._pointerlist[i2+1] = self._pointerlist[i2+1],self._pointerlist[i1+1]
                    return()
                elif v._k[1] == u1._k[1] and v._k[0] > u1._k[0]:
                    i1 = u1._k[0]
                    i2 = v._k[0]
                    v._k,u1._k= u1._k,v._k
                    self._pointerlist[i1+1],self._pointerlist[i2+1] = self._pointerlist[i2+1],self._pointerlist[i1+1]
                    return()
                return()
        elif u1._rc == None and u1._lc == None:
            return()
       
        
        while u1._rc._k[1] >= u1._k[1] or u1._lc._k[1] >= u1._k[1]:
            if u1._rc._k[1] > u1._lc._k[1]:
                v = u1._rc
            elif u1._rc._k[1] < u1._lc._k[1]:
                v = u1._lc
            elif u1._rc._k[1] == u1._lc._k[1] and u1._rc._k[0] < u1._lc._k[0]:
                v = u1._lc
            else:
                v = u1._rc
            
            i1 = u1._k[0]
            i2 = v._k[0]

            if v._k[1] == u1._k[1] and v._k[0] > u1._k[0]:
                v._k,u1._k= u1._k,v._k
                u1 = v
                self._pointerlist[i1+1],self._pointerlist[i2+1] = self._pointerlist[i2+1],self._pointerlist[i1+1]
            elif v._k[1] == u1._k[1] and v._k[0] < u1._k[0]:
                break
            else:
                v._k,u1._k= u1._k,v._k
                u1 = v
                self._pointerlist[i1+1],self._pointerlist[i2+1] = self._pointerlist[i2+1],self._pointerlist[i1+1]
            if v._rc == None or v._lc == None:
                break
        
        if u1._rc == None and u1._lc != None:
                v = u1._lc
                i1 = u1._k[0]
                i2 = v._k[0]
                if v._k[1] > u1._k[1]:
                    v._k,u1._k= u1._k,v._k
                    self._pointerlist[i1+1],self._pointerlist[i2+1] = self._pointerlist[i2+1],self._pointerlist[i1+1]
                    return()
                elif v._k[1] == u1._k[1] and v._k[0] > u1._k[0]:
                    v._k,u1._k= u1._k,v._k
                    self._pointerlist[i1+1],self._pointerlist[i2+1] = self._pointerlist[i2+1],self._pointerlist[i1+1]
                    return()
                return()
        else:
            return()
        
        
    
    # def minofHeap(self):
    #     m = self._root._k
    #     index = m[0]
    #     t = self._heap.pop()
    #     tp = t._p
    #     if t == tp._rc:
    #         tp._rc = self._root
    #         tp._rc._k[1] = float(inf)
    #         tp._rc._k[2] = m[1]
    #         self._heap.append(tp._rc)
    #     else:
    #         tp._lc = self._root
    #         tp._lc._k[1] = float(inf)
    #         tp._lc._k[2] = m[1]
    #         self._heap.append(tp._lc)
    #     # if index + 1 <= self._n -1:
    #     #     self._pointerlist[index+1]._k[2] = m[1]
    #     self._root._k = t._k
    #     self.heapdown(self._root)
    #     return(m)
    
    def changekey(self,u,v): #u is node, v is value #Can be optimised by seperating change key to each of i t and t' (eg: in case of change of t' we dont need heap up or heapdown)
        x = u._k
        u._k = v
    
        if v[1]< x[1]:
            self.heapdown(u)
        else:
            self.heapup(u)
        return()

    def BuildHeap(self,L):
        l = len(L)
        self._n = l #no of nodes = 0 initially
        
        for i in range(l):
            u = self.Node(L[i])
            if i == 0:
                u._p= None
            else:
                u._p = self._heap[(i-1)//2]
            self._heap.append(u)
        
        for j in range(l):
            if 2*j + 2 <= l-1:
                self._heap[j]._lc = self._heap[2*j+1]
                self._heap[j]._rc = self._heap[2*j+2]
            elif 2*j + 1 <= l-1:
                self._heap[j]._lc = self._heap[2*j+1]
            else:
                break

        self._pointerlist = self._pointerlist + self._heap
        
        for p in range((l-2)//2,-1,-1):
            self.heapdown(self._heap[p])

        self._root = self._heap[0] #root of heap 
        self._tail = self._heap[l-1] #last element of heap
        
        return(self._pointerlist) 
    
    def print_tree(self):   #O(n)
        i=0
        import math
        # print()
        while i<self._n:
            print(self._heap[i]._k,end=" ")
            k=math.log(i+2,2)
            if k==float(int(k)):
                print()
            i+=1
      
    


class Graph:
    def __init__(self,L):
        self._n = L[0]
        self._m = len(L[1])
        self._AdjList = self.BuildAdjList(L[1])
        self._source = L[2]
        self._target = L[3]
        self._Heap= MaxHeap()  #Heap object

        Ltest = []
        for i in range(self._n):
            if i == self._source:
                Ltest.append([i,float("inf")])
            else:
                Ltest.append([i,0])
        
        self._pointlist = MaxHeap.BuildHeap(self._Heap,Ltest) #gives pointer to node in heap given the index [note: index should be incremented by 1]
        # MaxHeap.print_tree(self._Heap)

    def BuildAdjList(self,inp):
        L1 = []
        for i in range(self._n):
            L1.append([])
        
        for j in range(self._m):
            v1 = inp[j][0]              #starting of edge
            v2 = inp[j][1]              #end point of edge
            c  = inp[j][2]              #capacity of that link
            L1[v1].append([v2,c]) #appending the endpoint of the edge and capacity of that link
            L1[v2].append([v1,c]) #appending the startpoint and capcity of link
        return(L1)


def findMaxCapacity(n,L,s,t):
    G = Graph([n,L,s,t])
    Adj_L = G._AdjList
    pointList = G._pointlist
    Heap = G._Heap
    capacity = 0
    parList = [0]*n

    # Heap.print_tree()
    # print("\n")

    while True:
        root = Heap._heap[0]
        c = root._k[1]
        v = root._k[0]
        
        Heap.changekey(root,[v,-1])
        
        # print("AdjList of",v,Adj_L[v])
        for j in Adj_L[v]:
            
            u = j[0]
            cap = j[1]

            # print("neighbour",u,"of",v)
            currentcap = pointList[u+1]._k[1]
            if currentcap != -1:
                if cap < c:
                    if currentcap < cap:
                        Heap.changekey(pointList[u+1],[u,cap])
                        parList[u] = v
                else:
                    if currentcap < c:
                        Heap.changekey(pointList[u+1],[u,c])
                        parList[u] = v
            # Heap.print_tree()
            # print("\n")
        
        # print(v)
        # Heap.print_tree()
        # print("\n")
        
        if v == t:
            capacity = c
            break
    Path = [t]
    par = parList[t]
    while True:
        Path.append(par)
        par = parList[par]
        if par == s:
            Path.append(par)
            break

        
    return(capacity,Path[::-1])

    

# findMaxCapacity(4,[(0,1,30),(0,3,10),(1,2,40),(2,3,50),(0,1,60),(1,3,50)],0,3)
# # (50,[0,1,3])
# findMaxCapacity(4,[(0,1,30),(1,2,40),(2,3,50),(0,3,10)],0,3)
# # (30,[0,1,2,3])
# findMaxCapacity(5,[(0,1,3),(1,2,5),(2,3,2),(3,4,3),(4,0,8),(0,3,7),(1,3,4)],0,2)
# # (4,[0,3,1,2])
# findMaxCapacity(7,[(0,1,2),(0,2,5),(1,3,4), (2,3,4),(3,4,6),(3,5,4),(2,6,1),(6,5,2)],0,5)
# # (4,[0, 2, 3, 5])
