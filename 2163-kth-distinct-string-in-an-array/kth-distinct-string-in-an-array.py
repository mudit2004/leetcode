class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        count = Counter(arr)
        distinct_count = 0

        for item in arr:
            if count[item] == 1:
                distinct_count += 1
                if distinct_count == k:
                    return item

        return ""