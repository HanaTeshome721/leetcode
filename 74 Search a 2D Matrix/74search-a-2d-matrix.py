class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #    row,col= len(matrix),len(matrix[0])
    #    t=0
    #    b=row-1

    #    while t<=b:
    #       rw=(t+b)//2
    #       if target>matrix[rw][-1]:
    #          t=rw+1
    #       elif target<matrix[rw][0]:
    #          b=rw-1
    #       else:
    #         break
    #    if not(t<=b):
    #       return False
    #    l=0
    #    r=col-1
    #    row=(t+b)//2  
    #    while l<r:
    #      m=(l+r)//2
    #      if target>matrix[row][m]:
    #          l=m+1
    #      elif target<matrix[row][m]:
    #         r=m-1
    #      else:
    #         return True
    #    return False      



       



        row=len(matrix)
        col=len(matrix[0])
        l=0
        rw=row*col-1

        while l<=rw:
            m=(l+rw)//2
            r=m//col
            c=m%col

            if target>matrix[r][c]:
                l=m+1
            elif target<matrix[r][c]:
                rw=m-1
            else:
                return True
        return False                