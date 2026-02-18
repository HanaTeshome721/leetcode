class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        cur=[]
        def back(indx):
            if indx==len(num):
                return len(cur)>=3
            for i in range(indx,len(num)):
                if num[indx]=="0" and i>indx:
                    break
                v=int(num[indx:i+1])
                if len(cur)>=2 and cur[-1]+cur[-2]!=v:
                    continue
                cur.append(v)
                if back(i+1):
                    return True
                cur.pop()
            return False     
        return back(0)
               

              