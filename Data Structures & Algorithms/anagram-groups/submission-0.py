class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            anagram = [0] * 26

            for c in word:
                anagram[ord(c) - ord('a')] += 1

            anagrams[tuple(anagram)].append(word)
        
        return list(anagrams.values())