class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ''
        for word in strs:
            string += str(len(word)) + '#' + word
        return string

    def decode(self, s: str) -> List[str]:
        output = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
        
            output.append(s[j + 1 : j + length + 1])
            i = j + length + 1
        
        return output