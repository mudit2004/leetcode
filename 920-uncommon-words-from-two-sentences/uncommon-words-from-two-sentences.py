from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = {}
        count = Counter(s1.split())
        count += Counter(s2.split())

        return [w for w in count if count[w] == 1]
        