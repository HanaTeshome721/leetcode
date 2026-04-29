class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         char=set()
         l=0
         mx=0
         for r in range(len(s)):
            while s[r] in char:
                char.remove(s[l])
                l+=1
            char.add(s[r])
            mx=max(mx,len(char))
         return mx   






        # see=set()
        # r=l=0
        # mx=0
        # while r<len(s):
        #     if s[r] not in see:
        #         see.add(s[r])
        #         mx=max(mx,r-l+1)
        #         r+=1
        #     else:
        #         see.remove(s[l])
        #         l+=1
        # return mx     

        # letter={}
        # curlen=0
        # mx=0
        # for i in range(len(s)):
        #     if s[i] in letter and letter[s[i]]>=i-curlen:
        #         curlen=i-letter[s[i]]   
        #     else:
        #         curlen+=1
        #         if mx<curlen:
        #             mx=curlen
        #     letter[s[i]]=i        
        # return mx                    


























        # # char=set()
        # # l=0
        # # mx=0
        # # for r in range(len(s)):
        # #     while s[r] in char:
        # #         char.remove(s[l])
        # #         l+=1
        # #     char.add(s[r])
        # #     mx=max(mx,r-l+1)
        # # return mx        
        
        # # seen=set()
        # # r=l=0
        # # mx=0
        # # while r<len(s):
        # #     if s[r] not in seen:
        # #         seen.add(s[r])
        # #         mx=max(mx,r-l+1)
        # #         r+=1
        # #     else:
        # #         seen.remove(s[l])
        # #         l+=1
        # # return mx 

        # letter={}
        # mx=0
        # curl=0

        # for i in range(len(s)):
        #     if s[i] in letter and letter[s[i]]>=i-curl:
        #         curl=i-letter[s[i]]
        #     else:
        #         curl+=1
        #         if mx<curl:
        #             mx=curl
        #     letter[s[i]]=i
        # return mx                          










     
    

				
				
				
				
				
				
				
				
				   
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				