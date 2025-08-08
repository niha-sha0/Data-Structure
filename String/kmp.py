class Solution(object):
    def compute_lps(self, pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        return lps

    
    def kmp_search(self, text, pattern):
        n = len(text)
        m = len(pattern)
        lps = self.compute_lps(pattern)

        i = j = 0

        while i < n:
            if text[i] == pattern[j]:
                i += 1
                j += 1

            if j == m:
                return True
            elif i < n and text[i] != pattern[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return False
        
    
    def stringMatching(self, words):
        res = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and self.kmp_search(words[j], words[i]):
                    res.append(words[i])
                    break

        return res
