class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += word + ":;"
        return encoded
    def decode(self, s: str) -> List[str]:
        word = ""
        decoded = []
        skip = False
        for count, letter in enumerate(s):
            if skip:
                word = ""
                skip = False
                continue

            if letter == ":" and s[count + 1] == ";":
                decoded.append(word)
                skip = True
            else:
                word += letter

        return decoded
