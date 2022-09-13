class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        answer: int = 0
        left, right = 0, len(tokens)-1
        while left <= right:
            target: int = tokens[left]
            if target <= power:
                answer += 1
                left += 1
                power -= target
            elif answer > 0:
                power += (tokens[right] - target)
                left += 1
                right -= 1
            else:
                break

        return answer
