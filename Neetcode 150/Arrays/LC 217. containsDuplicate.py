from black.trans import defaultdict


def containsDuplicate(nums):
    duplicate_hashmap = defaultdict(int)

    for i in nums:
        duplicate_hashmap[i] += 1

    for keys,values in duplicate_hashmap.items():
        if values > 1:
            return True

    return False


arr = [1,2,3,4]
print(containsDuplicate(arr))