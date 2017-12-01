#Given an array ‘A’ of sorted integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.
#
# Example: Input : 
#    A : [1 3 5] 
#    k : 4
# Output : YES as 5 - 1 = 4 
#Return 0 / 1 ( 0 for false, 1 for true ) for this problem
#
#Try doing this in less than linear space complexity.
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        if len(A)==0 or len(A)==1:
           return 0
        i = 0
        j = 1
        while(i != len(A)-1):
            if i == j:
                j = j+1
                if j ==  len(A):
                  break
            val = A[j] - A[i]
            if val == B:
                return 1
            elif val < B:
                j = j+1
                if j == len(A):
                  break
            elif val > B:
                i = i+1
        return 0
