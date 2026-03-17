class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
       f=0
       t=0
       for b in bills:
            if b==5:
                f+=1
            if b==10:
                t+=1
            change=b-5
            if change==5:
                if f>0:
                    f-=1
                else:
                    return False
            elif change==15:
                if f and t:
                    f-=1
                    t-=1
                elif f>=3:
                    f-=3
                else:
                    return False
       return True                    
