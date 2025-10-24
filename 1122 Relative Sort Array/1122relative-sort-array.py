class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # has=defaultdict(int)
        # for i in arr1:
        #     has[i]+=1
        # print(has) 
        # a12=[]
        # for v in arr2:
        #     t=has[v]
        #     for i in range(t): 
        #        a12.append(v)
        # lef=[]       
        # for v,i in has.items():
        #     if   v not in set(a12):
        #         a=[v]*i
        #         lef.extend(a)
        
        # lef.sort()
        # return a12+lef     



        
        # arr1c=defaultdict(int)
        # unique=[]

        # for v in arr1:
        #     if v in arr2:
        #         arr1c[v]+=1
        #     else:
        #         unique.append(v)
        # res=[]
        # for n in arr2:
        #     for _ in range(arr1c[n]) :
        #         res.append(n)
        # return res+ sorted(unique)                  




    #    a1c=Counter(arr1)
    #    res=[]
    #    for i in arr2:
    #       for _ in range(a1c.pop(i)):
    #         res.append(i)
    #    for i in range(min(arr1),max(arr1)+1):
    #      for _ in range(a1c.get(i,0)):
    #         res.append(i)
    #    return res          
          
       ar1c=Counter(arr1)
       res=[]
       for i in arr2:
         for _ in range(ar1c.pop(i)):
            res.append(i)
       for i in range(min(arr1),max(arr1)+1):
            for _ in range(ar1c.get(i,0)):
                res.append(i)
       return res        













