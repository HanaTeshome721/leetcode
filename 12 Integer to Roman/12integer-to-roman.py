class Solution:
    def intToRoman(self, num: int) -> str:
        # symlist=[ ["I",1], ["IV",4] ,["V",5], ["IX",9],
        #     ["X",10],["XL",40],["L",50],["XC",90],
        #     ["C",100], ["CD",400],["D",500],["CM",900],
        #     ["M",1000] 
        #     ] 
            
        # total=""
        # for r,n in reversed(symlist):
        #     an=num//n
        #     total+=an*r
        #     num=num%n
        # return total    
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        res=''
        for i in range(len(values)):
            while num>=values[i]:
                res+=symbols[i]
                num-=values[i]
        return res        


