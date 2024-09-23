def recursive(ind ,arr ,ans ,sub):
    if ind >= len(arr):
        ans.append(sub[:])
        return

    sub.append(arr[ind])
    recursive(ind+1,arr,ans,sub)
    sub.pop()
    recursive(ind + 1, arr, ans, sub)

def subset(arr):
    ans = []
    sub = []
    recursive(0,arr,ans,sub)

    return ans


nums = [1,2,3]
ans = subset(nums)
print(ans)

