class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # row=len(mat)
        # col=len(mat[0])
        # r=c=0
        # res=[]
        # d=1
        # for _ in range(row*col):
        #     res.append(mat[r][c])
        #     if d:
        #         if c==col-1:
        #             r+=1
        #             d=0
        #         elif r==0:
        #             c+=1
        #             d=0
        #         else:
        #             r-=1
        #             c+=1
        #     else:
        #         if r==row-1:
        #             c+=1
        #             d=1
        #         elif c==0:
        #             r+=1
        #             d=1
        #         else:
        #             r+=1
        #             c-=1
        # return res                      



           d=True
           c=r=0
           row=len(mat)
           col=len(mat[0])
           res=[] 
           while len(res)!=row*col:
              if d:
                while c<col and r>=0:
                    res.append(mat[r][c])
                    c+=1
                    r-=1
                if c==col:
                    r+=2
                    c-=1
                else:
                    r+=1
                
                d=False
              else:
                while r<row and c>=0:
                    res.append(mat[r][c])
                    r+=1
                    c-=1
                if r==row:
                    c+=2
                    r-=1
                else:
                    c+=1
                d=True                                
           return res

 
       