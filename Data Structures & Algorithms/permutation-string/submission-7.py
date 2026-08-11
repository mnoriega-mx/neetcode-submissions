class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_count = [0] * 26
        for c in s1:
            s1_count[ord(c) - ord('a')] += 1

        sub = [0] * 26
        for i in range(len(s1)):
            sub[ord(s2[i]) - ord('a')] += 1
        
        if s1_count == sub:
            return True

        i, j = 0, len(s1)
        while j < len(s2):
            sub[ord(s2[j]) - ord('a')] += 1
            sub[ord(s2[i]) - ord('a')] -= 1

            if sub == s1_count:
                return True

            i += 1
            j += 1

        return False