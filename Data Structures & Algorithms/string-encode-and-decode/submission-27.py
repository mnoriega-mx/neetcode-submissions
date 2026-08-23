class Solution:

    def encode(self, strs: List[str]) -> str:
        constructor = []
        for word in strs:
            constructor.append(str(len(word)))
            constructor.append('#')
            constructor.append(word)
        encoded = ''.join(constructor)

        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []

        i = j = 0
        while i < len(s):
            while s[j] != '#':
                j += 1

            length = int(s[i:j])

            i = j + 1
            j = i + length

            word = s[i:j]

            decoded.append(word)
            i = j
        
        return decoded