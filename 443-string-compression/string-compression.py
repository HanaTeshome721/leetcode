class Solution:
    def compress(self, chars: list[str]) -> int:
            lc=len(chars)
            r=0
            l=0
            while r<lc:
                cn=1
                while r<lc-1 and chars[r]==chars[r+1]:
                    r+=1
                    cn+=1
                chars[l]=chars[r]
                l+=1
                if cn>1:
                    for c in str(cn):
                        chars[l]=c
                        l+=1
                r+=1        
            return l   






            
 
      


    #   n=len(chars)
    #   l=0
    #   res=0
    #   for r in range(n+1):
    #     if r==n or chars[r]!=chars[l]:
    #         chars[res]=chars[l]
    #         res+=1
    #         cnt=r-l
    #         if cnt>1:
    #             for s in str(cnt):
    #                 chars[res]=s
    #                 res+=1
    #         l=r
    #   return res     



    #  chars.append('Exit')
    #  j=0
    #  perv=chars[0]
    #  n=len(chars)
    #  cnt=0
    #  for i in range(n):
    #     if perv==chars[i]:
    #         cnt+=1
    #     else:
    #         if cnt==1:
    #           chars[j]=perv
    #           j+=1
    #         else:
    #             chars[j]=perv 
    #             j+=1
    #             for n in str(cnt):
    #                 chars[j]=n
    #                 j+=1
    #         perv=chars[i]
    #         cnt=1
    #  return j                              