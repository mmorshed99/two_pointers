#Given an array and a value, remove all the instances of that value in the array. 
#Also return the number of elements left in the array after the operation.
#It does not matter what is left beyond the expected length.
#
# Example:
#If array A is [4, 1, 1, 2, 1, 3]
#and value elem is 1, 
#then new length is 3, and A is now [4, 2, 3] 
#Try to do it in less than linear additional space complexity.
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        i = 0
        j = 1
        while(i<len(A) and j < len(A)):
            if A[i] == B:
                if j <=i:
                    j = i+1
                    if j == len(A):
                        break
                while(j<len(A)):
                    if A[j] != B:
                        A[i],A[j] = A[j],A[i]
                        j = j +1
                        break
                    else:
                        j = j+1
            i = i+1
        count = 0
        for i in range(len(A)):
            if A[i] == B:
                break
            count +=1
        return count
