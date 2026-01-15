class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
       c=0
       word=set(word)
       for w in word:
         if w.lower()!=w and w.lower() in word:
            c+=1
         if w.upper()!=w and w.upper() in word:
            c+=1   
       return c//2    
