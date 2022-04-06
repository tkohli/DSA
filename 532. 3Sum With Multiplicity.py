class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        ans = 0
        arr.sort()
        for i, x in enumerate(arr):
            T = target - arr[i]
            j = i+1
            k = len(arr)-1
            while j < k:
                if arr[j] + arr[k] < T:
                    j += 1
                elif arr[j] + arr[k] > T:
                    k -= 1
                elif arr[j] != arr[k]:  # but arr[j] + arr[k] == T
                    #count left same number and right same number
                    left = right = 1
                    while j+1 < k and arr[j+1] == arr[j]:
                        left += 1
                        j += 1
                    while k-1 > j and arr[k-1] == arr[k]:
                        right += 1
                        k -= 1
                    ans += left * right
                    ans %= MOD
                    j += 1
                    k -= 1
                else:
                    # arr[i] == arr[k] and arr[j] + arr[k] == T
                    ans += (k-j+1) * (k-j)/2
                    ans %= MOD
                    break
        return int(ans)
