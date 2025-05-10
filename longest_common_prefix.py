class Solution:
    def longestCommonPrefix(self, v):
        if not v:
            return ""  

        
        prefix = v[0]

        for string in v:
            
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""  

        return prefix