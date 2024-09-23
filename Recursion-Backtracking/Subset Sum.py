def recursive(ind,n,arr,ans,sub):
        if ind >= n:
            ans.append(sub)
            return
        recursive(ind+1,n,arr,ans,sub+arr[ind])
        recursive(ind + 1, n, arr, ans, sub)
def subsetsum(n,arr):
    ans = []
    sub = 0
    recursive(0,n,arr,ans,sub)
    return ans


n = 2
arr = [2,3]
ans = subsetsum(n,arr)
print(ans)