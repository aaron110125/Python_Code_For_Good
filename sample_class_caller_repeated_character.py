class Solution:
    def repeatedCharacter(self, s: str) -> str:
        unique_letter = []

        for i in range(len(s)):
            if (s[i]) not in unique_letter:
                unique_letter.append(s[i])
            else:
                return (s[i])
                break

r = Solution().repeatedCharacter("abdcca")
print(r)
