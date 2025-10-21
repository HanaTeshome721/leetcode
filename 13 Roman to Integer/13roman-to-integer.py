class Solution:
    def romanToInt(self, s: str) -> int:
        # d={
        # "I": 1,
        # "V": 5,
        # "X": 10,
        # "L": 50,
        # "C": 100,
        # "D": 500,
        # "M": 1000
        # }
        # out=0
        # for i in range(len(s)):
        #     if i <len(s)-1 and d[s[i]]<d[s[i+1]]:
        #         out-=d[s[i]]
        #     else:
        #         out+=d[s[i]]  
        # return out          
        # re=0
        # n=len(s)
        # i=0
        # while i<n:
        #     if i<n-1 and d[s[i]]<d[s[i+1]]:
        #         re+=d[s[i+1]]-d[s[i]]
        #         i+=2
        #     else:
        #         re+=d[s[i]]
        #         i+=1
        # return re            
  
       roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
       total=0
       per=0

       for ch in reversed(s):
            val=roman[ch]
            if val<per:
                total-=val
            else:
                total+=val
            per=val
       return total     
                    











        # out=0
        # for i in range(len(s)):
        #     if i<len(s)-1 and d[s[i]] < d[s[i+1]]:
        #         out-=d[s[i]]
        #     else:
        #         out+=d[s[i]]   
        # return out         

        # d={"I": 1,
        #     "V": 5,
        #     "X": 10,
        #     "L": 50,
        #     "C": 100,
        #     "D": 500,
        #     "M": 1000
        #     }

        # summ=0
        # i=0
        # n=len(s)
        # while i <n:
        #     if i<n-1 and d[s[i]]<d[s[i+1]]:
        #         summ+=d[s[i+1]]-d[s[i]]
        #         i+=2
        #     else:
        #         summ+=d[s[i]]
        #         i+=1    
        # return summ      