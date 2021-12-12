nums = [1, 3, 5, 6]
target = 2
left, right = 0, len(nums)-1
while left <= right:
    mid = left+(right-left)//2
    if nums[mid] == target:
        print(mid+"gg")
        break
    elif nums[mid] > target:
        right = mid-1
    else:
        left = mid+1
if(nums[mid] > target):
    print(left)
elif(nums[mid] < target):
    print(mid+1)
