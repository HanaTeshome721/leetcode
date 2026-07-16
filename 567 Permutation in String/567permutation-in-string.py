class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # n1=len(s1)
        # n2=len(s2)
        # c1=Counter(s1)
        # c2=Counter(s2[:n1])

        # l=0
        # if c1==c2:
        #     return True
        # for r in range(n1,n2):
        #     c2[s2[r]]+=1
        #     c2[s2[l]]-=1
        #     l+=1
        #     if c2[s2[l]]==0:
        #         del c2[s2[l]]
        #     if c1==c2:
        #         return True
        # return False  
        
       l1 ,l2 =len(s1) ,len(s2)

       if l1>l2:
        return False

       cs1,cs2=[0]*26 ,[0]*26
       for i in range(l1):
        cs1[ord(s1[i]) - ord('a')]+=1
        cs2[ord(s2[i])- ord('a')] +=1
       matches=0
       for i in range(26):
         matches+=1 if cs1[i]==cs2[i] else 0
       l=0
       for r in range(l1,l2):
          if cs1==cs2: return True
          index=ord(s2[r]) - ord('a')
          cs2[index]+=1
          if cs2[index]==cs1[index]:
            matches+=1
          elif cs2[index]==cs1[index]+1:
            matches-=1

          index=ord(s2[l]) - ord('a')
          cs2[index]-=1
          if cs1[index]==cs2[index]:
            matches+=1
          if cs2[index]==cs1[index]-1:
            matches-=1

          l+=1
       return matches==26          

          




        
                  