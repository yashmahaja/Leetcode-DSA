def containsDuplicate(nums):
    track = set(nums)
    return not len(track) == len(nums)

