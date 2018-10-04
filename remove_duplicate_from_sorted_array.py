int Solution::removeDuplicates(vector<int> &A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    if(A.size() == 0){
        return A.size();
    }
    
    int j = 0;
    for(int i = 1; i < A.size(); i++){
        if(A[j] != A[i]){
            A[j+1] = A[i];
            j++;
        }
    }
    
    A.erase(A.begin()+j+1, A.end());
    return j+1;
}
