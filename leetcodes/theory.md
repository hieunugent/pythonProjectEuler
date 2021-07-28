# backtracking:
- technique for solving problems recursively by trying to build a solution incrementally, one peach at a time, removing those solutions that fail to satisfy the constraints of the problems at any point in time 
- can be defined as a general algorithmic technique that considers searching every possible combination in order to solve a computational problem
- Decision Problem – In this, we search for a feasible solution.
- Optimization Problem – In this, we search for the best solution.
- Enumeration Problem – In this, we find all feasible solutions.
- how to determine this is backtracking problem
    - The Algorithm begins to build up a solution, starting with an empty solution set S . S = {} 

        - Add to S  the first move that is still left (All possible moves are added to S  one by one). This now creates a new sub-tree s  in the search tree of the algorithm.
        - Check if S+s  satisfies each of the constraints in C  . 
            - If Yes, then the sub-tree s  is “eligible” to add more “children”.
            - Else, the entire sub-tree s  is useless, so recurs back to step 1 using argument S  .
        - In the event of “eligibility” of the newly formed sub-tree s, recurs back to step 1, using argument S+s .
        - If the check for S+s  returns that it is a solution for the entire data D . Output and terminate the program. 
        - If not, then return that no solution is possible with the currents and hence discard it.
- Difference between Recursion and Backtracking:
    - In recursion, the function calls itself until it reaches a base case. In backtracking, we use recursion to explore all the possibilities until we get the best result for the problem.
- backtracking is an algorithm for finding all solutions by exploring all potential candidates. If the solution candidate. If the solution candidate turn s to be not a solution or at least not the last one. backtracking algorithm discard it by making some changes on the previous step, i.e backtracks and then try again
# Dynamic Program 
# Greedy Algorithms
# heap Queue in Python 
- the property of this data structure in python is that each time the smallest of heap element  is popped(min heap)
- whenever elements are pushed or popped, heap structure in maintained
- the heap[0] element also return the smallest each time
- heapify : this function is used to convert the iterable into a heap data structure in heap order
- heappush(heap, ele): this function is used to insert the element mentioned in its arguments into heap. the order is adjusted so as heap structure is maintained 
- heappop(heap) ; this function is used to removed and return the smallest element from heap. the order is adjusted , so as heap structure is maintained
- heappushpop(heap, ele) :- This function combines the functioning of both push and pop operations in one statement, increasing efficiency. Heap order is maintained after this operation. 
- heapreplace(heap, ele) :- This function also inserts and pops element in one statement, but it is different from above function. In this, element is first popped, then the element is pushed.i.e, the value larger than the pushed value can be returned. heapreplace() returns the smallest value originally in heap regardless of the pushed element as opposed to heappushpop().
- nlargest(k, iterable, key = fun) :- This function is used to return the k largest elements from the iterable specified and satisfying the key if mentioned.
- nsmallest(k, iterable, key = fun) :- This function is used to return the k smallest elements from the iterable specified and satisfying the key if mentioned.