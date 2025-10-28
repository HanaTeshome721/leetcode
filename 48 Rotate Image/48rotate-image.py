class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # row=len(matrix)
        # for r in range(row):
        #     for c in range(r+1,row):
        #         matrix[c][r],matrix[r][c]=matrix[r][c],matrix[c][r]
        # for r in matrix:
        #     r.reverse()        
        r=len(matrix)-1
        l=0
        while l<r:
           
            for i in range(r-l):
                t,b=l,r
                tl=matrix[t][l+i]
                matrix[t][l+i]=matrix[b-i][l]
                matrix[b-i][l]=matrix[b][r-i]
                matrix[b][r-i]=matrix[t+i][r]
                matrix[t+i][r]=tl
            l+=1
            r-=1
