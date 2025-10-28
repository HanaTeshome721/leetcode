class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # row=len(img)
        # col=len(img[0])
        # res=[[0]*col for _ in range(row)]
        # for  r in range(row):
        #     for c in range(col):

        #         total=0
        #         cnt=0
        #         for i in [r-1,r,r+1]:
        #             for j in [c-1,c,c+1]:
        #                 if i==row or j==col or i<0 or j<0:
        #                     continue
        #                 total+=img[i][j]
        #                 cnt+=1
        #         res[r][c]=total//cnt
        # return res   


        rows=len(img)
        cols=len(img[0]) 
        res=[[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                s=img[i][j]
                c=1
                if i-1>-1:
                    s+=img[i-1][j]
                    c+=1
                if i+1<rows:
                    s+=img[i+1][j]
                    c+=1
                if j-1>-1:
                    s+=img[i][j-1]
                    c+=1
                if j+1<cols:
                    s+=img[i][j+1]
                    c+=1
                if i-1>-1 and j-1>-1:
                    s+=img[i-1][j-1]
                    c+=1
                if i-1>-1 and j+1<cols:
                    s+=img[i-1][j+1]
                    c+=1
                if i+1<rows and j-1>-1:
                    s+=img[i+1][j-1]
                    c+=1
                if i+1<rows and j+1<cols:
                    s+=img[i+1][j+1]
                    c+=1                    
                
                res[i][j]=s//c
        return res            
        