class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # perif=[0]*(len(s)+1)

        # for l,r,d in shifts:
        #     perif[r+1]+=1 if d else -1
        #     perif[l]+=-1 if d else 1
        # res=[ord(c)-ord('a') for c in s]
        # diff=0
        # for i in reversed(range(len(perif))):
        #     diff+=perif[i]
        #     res[i-1]= (diff+ res[i-1] )%26
        # s=[chr(ord('a') +n ) for n in res]
        # return ''.join(s)      
    

    #    diff=[0]*(len(s)+1)

    #    for l,r,d in shifts:
    #     de=1
    #     if d==0:
    #         de=-1
    #     diff[l]+=de
    #     diff[r+1]-=de
    #    ans=[] 
    #    for c,sh in zip(s,accumulate(diff)):
    #     asci=(ord(c) -ord('a') +sh)%26
    #     ans.append(chr(ord('a')+asci))
    #    return ''.join(ans) 

       dif=[0]*(len(s)+1)

       for l,r,d in shifts:
        de=1 if d else -1
        dif[l]+=de
        dif[r+1]-=de
       ans=[]
       run=0
       for i,v in enumerate(s):
         run+=dif[i]
         code=(ord(v)-ord('a')+ run) %26
         ans.append(chr(ord('a') + code))
       return ''.join(ans)   





















       
          

           

    