class Solution:
    def romanToInt(self, s: str) -> int:
        dct={
            "I": 1,
           "V" : 5,
            "X" : 10,
            "L"  :50,
            "C"  :100,
            "D" : 500,
            "M"  :1000,
        }
        cnt=0
        for i in range(len(s)-1):
            print(cnt)
            if dct[s[i]]>=dct[s[i+1]]:
               cnt+=dct[s[i]]
            else:
                cnt-=dct[s[i]]
        cnt+=dct[s[-1]]        
        return cnt    