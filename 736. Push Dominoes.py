dominoes = ".L.R...LR..L.."


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        temp = ''

        while dominoes != temp:
            temp = dominoes
            dominoes = dominoes.replace('R.L', 'xxx')       # <-- 1)
            dominoes = dominoes.replace('R.', 'RR')         # <-- 2)
            dominoes = dominoes.replace('.L', 'LL')         # <-- 2)

        return dominoes.replace('xxx', 'R.L')              # <-- 3)

        # d = 'L' + dominoes + 'R'
        # res = ""
        # i = 0
        # for j in range(1, len(d)):
        #     if d[j] == '.':
        #         continue
        #     middle = j - i - 1
        #     if i:
        #         res += d[i]
        #     if d[i] == d[j]:
        #         res += d[i] * middle
        #     elif d[i] == 'L' and d[j] == 'R':
        #         res += '.' * middle
        #     else:
        #         res += 'R' * (middle // 2) + '.' * (middle %
        #                                             2) + 'L' * (middle // 2)
        #     i = j
        # return "".join(res)
