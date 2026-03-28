def hasDuplicate(nums):
    if len(nums) == len(set(nums)):
        return False
    else:
        return True


def hasDuplicate_fast(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False
