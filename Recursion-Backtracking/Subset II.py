
def recursive(ind ,arr ,ans ,sub):
    if ind >= len(arr):
        ans.append(sub[:])
        return

    sub.append(arr[ind])
    recursive(ind+1,arr,ans,sub)
    sub.pop()
    while ind+1 < len(arr) and arr[ind] == arr[ind + 1]:
        ind +=1
    recursive(ind + 1, arr, ans, sub)
def subsetII(arr):
    ans = []
    sub = []
    recursive(0,arr,ans,sub)
    return ans


nums = [1,2,2]
nums.sort()
ans = subsetII(nums)
print(ans)

