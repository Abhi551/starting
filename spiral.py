class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        n , m , p , q = len(A) - 1 , len(A[0]) - 1  , 0 , 0;
        list_of_int = [];

        if len(A) == 1:
        	print (A[0])
        	return A[0]
        for count in range(n):

            for j in range(0 , m+1):
                i=0;
                if A[p][j] != 9999:
                    print A[p][j];
                    list_of_int.append(A[p][j]);
                    A[p][j] = 9999;
            p = p+1;
        
            for i in range(0 , n+1):
                if A[i][m]!= 9999:
                    #print (a[i][m]);
                    list_of_int.append(A[i][m]);
                    A[i][m] = 9999;
        
            m = m-1;
        
            for j in range(m , -1 , -1):
                if A[n][j] != 9999:
                    #print (a[n][j])
                    list_of_int.append(A[n][j]);
                    A[n][j] = 9999;
            n=n-1;
                    
        #print (a);
        print (list_of_int)
        return(list_of_int)


A =[
  [1, 2],
  [3, 4],
  [5, 6]
	]
"""
A = [
	[1]
	]
"""
#print (len(A))
#print (len(A[0]))
s = Solution();
s.spiralOrder(A)