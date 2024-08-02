class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        
        for word in strs:
            char_count = [0] * 26

            for letter in word:
                position = ord(letter) - ord("a")
                char_count[position] += 1
        
            char_count = tuple(char_count)
            anagram_dict[char_count] = anagram_dict.get(char_count, []) + [word]
        
        return anagram_dict.values()
