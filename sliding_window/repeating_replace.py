s = "XYYX"
k = 2


def characterReplacement(s: str, k: int) -> int:
    res = 0
    left = 0
    count = {}
    for right, i in enumerate(s):
        count[i] = 1 + count.get(i, 0)
        while (right - left + 1) - max(count.values()) > k:
            count[s[left]] -= 1
            left += 1
        res = max(res, right - left + 1)
    return res


print(characterReplacement(s, k))
