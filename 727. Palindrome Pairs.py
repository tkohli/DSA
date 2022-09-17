class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result = []

        # Store all words and reversals.
        ws = []
        for i, word in enumerate(words):
            ws.append((word,       False, i, len(word)))
            ws.append((word[::-1], True,  i, len(word)))
        ws.sort()

        for i, (a, a_reversed, a_idx, a_len) in enumerate(ws):
            for j in range(i + 1, len(ws)):
                b, b_reversed, b_idx, _ = ws[j]
                if b.startswith(a):
                    if a_idx != b_idx and a_reversed != b_reversed:
                        rest = b[a_len:]
                        if rest == rest[::-1]:
                            result.append(
                                [a_idx, b_idx] if b_reversed else [b_idx, a_idx])
                else:
                    break
        return result


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        mp = {}
        ans = []
        for i in range(0, len(words)):
            mp[words[i]] = i
        for j in range(0, len(words)):
		##case 1: if the reverse of given word is present in words set
            if (words[j][::-1]) in mp and mp[words[j][::-1]] != j:
                ans.append([j, mp[words[j][::-1]]])
		## case2: if the given word is palindrome and the word set also contains the "" (empty) word
            if words[j] != "" and "" in mp and words[j] == words[j][::-1]:
                ans.append([mp[""], j])
                ans.append([j, mp[""]])
		## case3: if word from wordset after being adding to start or at last forms a palindromic pairs
            for i in range(1, len(words[j])):
                if words[j][i:][::-1] in mp and (words[j][:i] == words[j][:i][::-1] and mp[words[j][i:][::-1]] != j):
                    ans.append([mp[words[j][i:][::-1]], j])
                if words[j][:i][::-1] in mp and (words[j][i:] == words[j][i:][::-1] and mp[words[j][:i][::-1]] != j):
                    ans.append([j, mp[words[j][:i][::-1]]])

        return ans
