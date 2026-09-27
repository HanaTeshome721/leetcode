class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
     ans=[]
     inb=False

     for line in source:
        i=0
        if not inb:
            new=[]
        while i<len(line):
            if line[i:i+2]=="/*" and not inb:
                inb=True
                i+=1
            elif line[i:i+2]=="*/" and inb:
                inb=False
                i+=1
            elif not inb and line[i:i+2]=="//":
                break
            elif not inb:
                new.append(line[i])
            i+=1
        if new and not inb:
            ans.append("".join(new))
     return ans                               