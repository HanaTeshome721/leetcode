class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # return len(set(s))==len(set(t))
        mp={}
        if len(s)>len(t):
            return False
        l=len(s)
        st=set()    
        for i in range(l):
          if s[i] in mp and mp[s[i]] != t[i]: 
                return False
          elif s[i] not in mp and t[i] in st: 
                return False     
          else:
            mp[s[i]]=t[i]     
            st.add(t[i]) 
        print(mp)               
        return True                        