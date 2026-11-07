class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        char_counts = {}
        for char in magazine:
            char_counts[char] = char_counts.get(char, 0) + 1

        for char in ransomNote:
            if char_counts.get(char, 0) <= 0:
                return False
            char_counts[char] -= 1

        return True