import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Normalize paragraph: lowercase, replace punctuation with space
        words = re.findall(r'\w+', paragraph.lower())
        
        # Convert banned list to set for faster lookup
        banned_set = set(banned)
        
        # Count non-banned words
        counts = Counter(word for word in words if word not in banned_set)
        
        # Return the word with the highest count
        return counts.most_common(1)[0][0]
