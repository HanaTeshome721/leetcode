class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
       if len(s2)<len(s1):
        return False 
       s1c={}      
       s2c={}

       for i in range(len(s1)):
            s1c[s1[i]]=1+ s1c.get(s1[i],0)      
            s2c[s2[i]]=1+ s2c.get(s2[i],0)   
       if s1c==s2c:
        return True
       j=0 
       for i in range(len(s1),len(s2)):
             s2c[s2[i]]=1+ s2c.get(s2[i],0) 
             s2c[s2[j]]-=1

             if s2c[s2[j]]==0:
                s2c.pop(s2[j])
             j+=1    
             if s1c==s2c:
                return True
       return  False                               