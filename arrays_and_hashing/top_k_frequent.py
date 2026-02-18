from collections import defaultdict


def topKFrequent(nums, k):
    counter = {}
    result = defaultdict(list)
    freq = []
    for i in nums:
        counter[i] = 1 + counter.get(i, 0)
    for key, value in counter.items():
        result[value].append(key)
    for i in range(len(nums), 0, -1):
        if i in result:
            freq.extend(result[i])
        if len(freq) >= k:
            break

    return freq[:k]
