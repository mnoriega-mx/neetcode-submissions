class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        for i in s1:
            s1_count[ord(i) - ord('a')] += 1

        window = [0] * 26
        for i in range(len(s1)):
            window[ord(s2[i]) - ord('a')] += 1


        l, r = 0, len(s1) - 1
        while r < len(s2):
            if s1_count == window:
                return True

            window[ord(s2[l]) - ord('a')] -= 1
            l += 1

            r += 1
            if r < len(s2):
                window[ord(s2[r]) - ord('a')] += 1

        return False