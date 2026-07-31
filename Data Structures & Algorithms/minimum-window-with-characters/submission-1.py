class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map, window = {}, {}
        
        for i in t:
            t_map[i] = t_map.get(i, 0) + 1
        
        shortest = ''
        matches = 0
        needed_matches = len(t_map)

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in t_map and window[c] == t_map[c]:
                matches += 1
            
            while matches == needed_matches:
                subs = s[l : r + 1]
                if shortest == '' or len(subs) < len(shortest):
                    shortest = subs
                
                left_c = s[l]
                window[left_c] -= 1
                if left_c in t_map and window[left_c] < t_map[left_c]:
                    matches -= 1
                l += 1

        return shortest