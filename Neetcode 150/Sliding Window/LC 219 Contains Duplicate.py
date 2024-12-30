import collections


def containsduplicate(nums,k):
    keys = collections.defaultdict(int)
    i = 0
    j = 0
    for pointer in range(k+1):
        j += 1
        keys[nums[pointer]] += 1

    for point in range(j,len(nums)):
        print(point)
        # print(len(nums))
        keys[nums[i]] -= 1
        i += 1
        keys[nums[point]] += 1
        print(keys,"j")

    for k,v in keys.items():
        if v > 1:
            return True
        else:
            return False




nums = [1,0,1,1]
k = 1
ans = containsduplicate(nums,k)
print(ans)