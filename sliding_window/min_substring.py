from collections import Counter

s = "OUZODYXAV"
t = "XYZ"


def minWindow(s: str, t: str) -> str:
    left = 0
    count = Counter(t)
    need = len(count)
    have = 0
    res, res_len = [-1, -1], float("inf")
    window_count = {}

    for right, i in enumerate(s):
        window_count[i] = 1 + window_count.get(i, 0)
        if i in count and window_count[i] == count[i]:
            have += 1

        while have == need:
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = right - left + 1
            left_char = s[left]
            window_count[left_char] -= 1

            if left_char in count and window_count[left_char] < count[left_char]:
                have -= 1

            left += 1

    l, r = res
    return s[l : r + 1] if res_len != float("inf") else ""


print(minWindow(s, t))
