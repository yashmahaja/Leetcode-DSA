def recursive(ind ,arr ,ans ,sub,target):
    if ind >= len(arr):
        if target == 0:
            ans.append(sub[:])
        return

    if arr[ind] <= target:
        sub.append(arr[ind])
        recursive(ind,arr,ans,sub,target-arr[ind])
        sub.pop()

    recursive(ind + 1, arr, ans, sub, target)

def combination(arr,target):
    ans = []
    sub = []
    recursive(0,arr,ans,sub,target)
    return ans

candidates = [2,3,6,7]
target = 7
ans = combination(candidates,target)
print(ans)