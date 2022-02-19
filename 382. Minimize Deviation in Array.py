import heapq
heap = []
nums = [1, 2, 3, 4]
pq = []
for a in nums:
    heapq.heappush(pq, -a * 2 if a % 2 else -a)
res = float('inf')
mi = -max(pq)
while len(pq) == len(nums):
    a = -heapq.heappop(pq)
    res = min(res, a - mi)
    if a % 2 == 0:
        mi = min(mi, a / 2)
        heapq.heappush(pq, -a / 2)
# for num in nums:
#     # we double all odd number first
#     heapq.heappush(heap, -num * 2 if num % 2 else -num)
# res = float("inf")
# mi = -max(heap)  # this is actually the min val
# for num in nums:
#     a = heapq.heappop(heap)
#     res = min(res, mi-a)
#     if a % 2 == 0:
#         mi = min(mi, a//2)
#         heapq.heappush(heap, -a/2)
print(int(res))
