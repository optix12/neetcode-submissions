class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            for j in i:
                encoded += str(ord(j))
                encoded += "$"
            encoded += "-"
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        builder=""
        stringAdd = ""
        i = 0
        while i < len(s):
            if s[i] == "-":
                decoded.append(stringAdd)
                stringAdd = ""

            else:
                while s[i] != "$":
                    builder += s[i]
                    i+= 1
                stringAdd += chr(int(builder))
                builder = ""
            i += 1
        return decoded
                



