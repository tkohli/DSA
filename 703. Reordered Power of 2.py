class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        return sorted(str(N)) in [sorted(str(2**i)) for i in range(30)]
        # we could have also used counter
