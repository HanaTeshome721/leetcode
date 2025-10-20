class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # c=[0]*60
        # for s,e in ranges:
        #     for i in range(s,e+1):
        #         c[i]=1
        # for i in range(left ,right + 1):
        #     if not c[i]:
        #         return False
        # return True 

        # given=[i for i in range(left,right+1)]
        # for s,e in ranges:
        #     for i in range(s,e+1):
        #         if i in given:
        #             given.remove(i)
        # return False if given else True   

        c={}
        for s,e in ranges:
            for i in range(s,e+1):
                c[i]=None
        for i in range(left,right+1):
            if  i not in c:
                return False
        return True                


