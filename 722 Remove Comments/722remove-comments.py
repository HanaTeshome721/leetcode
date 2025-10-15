class Solution:
    def removeComments(self, source: List[str]) -> List[str]:                                
    #    ans=[]
    #    in_block=False
    #    for line in source:
    #      i=0
    #      if not in_block:
    #        new=[]
    #      while i< len(line):
    #        if line[i:i+2]=="/*" and not in_block:
    #          in_block=True
    #          i+=1
    #        elif line[i:i+2]=="*/" and in_block:
    #          in_block=False
    #          i+=1
    #        elif not in_block and line[i:i+2]=='//':
    #              break
    #        elif  not in_block:
    #            new.append(line[i])
    #        i+=1 
    #      if new and not in_block:
    #         ans.append(''.join(new))
         
    #    return ans

      res=[]
      mc=False
      for line in source:
        attach=mc
        perv=''
        i=0
        while i<len(line):
            d=line[i:i+2]
            if d=="/*" and mc is False:
                i+=2
                mc=True
                continue
            elif d=="*/" and mc is True:
                i+=2
                mc=False
                continue
            elif d=='//' and mc is False:
                break
            elif mc is False:
                perv+=line[i]
            i+=1
        if attach:
            res.append(res.pop()+perv)
        else:
            res.append(perv)
      return list(filter(None,res))                             