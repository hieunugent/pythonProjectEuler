# backtracking:
- technique for solving problems recursively by trying to build a solution incrementally, one peach at a time, removing those solutions that fail to satisfy the constraints of the problems at any point in time 
- can be defined as a general algorithmic technique that considers searching every possible combination inorder to solve a computational problem
- Decision Problem – In this, we search for a feasible solution.
- Optimization Problem – In this, we search for the best solution.
- Enumeration Problem – In this, we find all feasible solutions.
- how to determine this is backtracking problem
    - The Algorithm begins to build up a solution, starting with an empty solution set S  . S = {} 

        - Add to S  the first move that is still left (All possible moves are added to S  one by one). This now creates a new sub-tree s  in the search tree of the algorithm.
        - Check if S+s  satisfies each of the constraints in C  . 
            - If Yes, then the sub-tree s  is “eligible” to add more “children”.
            - Else, the entire sub-tree s  is useless, so recurs back to step 1 using argument S  .
        - In the event of “eligibility” of the newly formed sub-tree s  , recurs back to step 1, using argument S+s  .
        - If the check for S+s  returns that it is a solution for the entire data D  . Output and terminate the program. 
        - If not, then return that no solution is possible with the current s  and hence discard it.
- Difference between Recursion and Backtracking:
    - In recursion, the function calls itself until it reaches a base case. In backtracking, we use recursion to explore all the possibilities until we get the best result for the problem.

# Dynamic Program 
# Greedy Algorithms
