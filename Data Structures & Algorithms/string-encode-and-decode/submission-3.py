class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for i in strs:
            encoded.append(str(len(i)))
            encoded.append("#")
            encoded.append(i)
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        arr = []
        i = 0

        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            i = j + 1
            j = i + length
            arr.append(s[i:j])
            i = j

        return arr


                



