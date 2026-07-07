from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # Build Trie
        root = {}
        
        # Insert words with their indices
        for word in words:
            node = root
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['#'] = node.get('#', 0) + 1  # count of words ending here
        
        # Process string s
        count = 0
        # BFS/DFS over string s
        queue = [(root, 0)]  # (node, start_index)
        
        while queue:
            node, idx = queue.pop()
            
            # If this node has words ending here, add to count
            count += node.get('#', 0)
            
            # For next character
            if idx >= len(s):
                continue
            
            # For each possible next character in trie
            for c in node:
                if c == '#':
                    continue
                # Find next occurrence of c in s starting from idx
                next_idx = s.find(c, idx)
                if next_idx != -1:
                    queue.append((node[c], next_idx + 1))
        
        return count





        # self.count = 0  # Use instance variable to track count
        
        # def dfs(node, start_idx):
        #     """DFS to process all words in the trie starting from given node"""
            
        #     # Add count of words ending at this node
        #     self.count += node.get('#', 0)
            
        #     # If we've reached the end of s, stop (no more characters to match)
        #     if start_idx >= len(s):
        #         return
            
        #     # Try each child character
        #     for c in node:
        #         if c == '#':
        #             continue
                
        #         # Find next occurrence of character c in s starting from start_idx
        #         next_idx = s.find(c, start_idx)
        #         if next_idx != -1:
        #             # Recursively process the child node
        #             dfs(node[c], next_idx + 1)
        
        # # Start DFS from root with index 0
        # dfs(root, 0)
        
        # return self.count
