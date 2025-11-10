class Solution:
    def validPalindrome(self, s: str) -> bool:
        #    l,r=0,len(s)-1
        #    while l<r:
        #       if s[l]!=s[r]:
        #         skipl=s[l+1:r+1]
        #         skipr=s[l:r] 
        #         return (skipl==skipl[::-1] or skipr==skipr[::-1])
        #       l+=1
        #       r-=1
        #    return True  

       
            # def palinderome(l,r):
               
            #         while l<r:
            #            if s[l]!=s[r]:
            #                 return False
            #            l+=1
            #            r-=1
            #         return True
            # l=0
            # r=len(s)-1
            # while l<r:
            #     if s[l]!=s[r]:

            #       return palinderome(l+1,r) or palinderome(l,r-1)
            #     l+=1
            #     r-=1  
            # return True         

            if s==s[::-1]:
               return True

            i=0
            j=len(s)-1
            while i<=j:
                if s[i]!=s[j]:
                    break
                i+=1
                j-=1    
            x=s[:i] +s[i+1:]
            if x==x[::-1]:
                return True 
            y=s[:j]+s[j+1:]
            if y==y[::-1]:
               return True
            return False            
                            


















