from collections import Counter

s1 = "abc"
s2 = "lecabee"


def checkInclusion(s1: str, s2: str) -> bool:
    left = 0
    count = Counter(s1)
    window_count = {}
    for right, i in enumerate(s2):
        window_count[s2[right]] = 1 + window_count.get(s2[right], 0)
        if right + 1 - left == len(s1):
            if window_count != count:
                window_count[s2[left]] -= 1
                if window_count[s2[left]] == 0:
                    window_count.pop(s2[left])
                left += 1
            else:
                return True
    return False


print(checkInclusion(s1, s2))
