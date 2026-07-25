class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for string in strs:
            encoded += str(len(string))+ '#' + string
        
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            decoded.append(s[j+1 : j + 1 + int(s[i:j])])
            i = j + 1 + int(s[i:j])

        return decoded