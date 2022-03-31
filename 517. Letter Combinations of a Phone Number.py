class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        dct = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        if digits == "":
            return []
        ans = ['']
        for digit in digits:
            tmp = dct[int(digit)]
            ans2 = []
            for n in ans:
                for m in tmp:
                    ans2.append(n+m)
            ans = ans2
        return ans

class Solution:
    def letterCombinations(self, phoneNumber: str) -> List[str]:
        if phoneNumber == '':
            return []

        def phoneNumberMnemonicsHelper(idx, phoneNumber, currentMnemonics, honeMnemonics):
            if idx == len(phoneNumber):
                phoneMnemonics.append("".join(currentMnemonics))
            else:
                currentDigit = phoneNumber[idx]
                letter = number_Digit[currentDigit]
                for i in range(len(letter)):
                    currentMnemonics[idx] = letter[i]
                    phoneNumberMnemonicsHelper(
                        idx+1, phoneNumber, currentMnemonics, phoneMnemonics)

        number_Digit = {
            "0": ["0"],
            "1": ["1"],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        currentMnemonics = ["0"]*len(phoneNumber)
        phoneMnemonics = []
        phoneNumberMnemonicsHelper(
            0, phoneNumber, currentMnemonics, phoneMnemonics)
        return phoneMnemonics
