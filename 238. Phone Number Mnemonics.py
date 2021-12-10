def phoneNumberMnemonics(phoneNumber):
    currentMnemonics = ["0"]*len(phoneNumber)
    phoneMnemonics = []
    phoneNumberMnemonicsHelper(
        0, phoneNumber, currentMnemonics, phoneMnemonics)
    return phoneMnemonics


def phoneNumberMnemonicsHelper(idx, phoneNumber, currentMnemonics, phoneMnemonics):
    if idx == len(phoneNumber):
        mnemonics = "".join(currentMnemonics)
        phoneMnemonics.append(mnemonics)
    else:
        digit = phoneNumber[idx]
        letters = number_Digit[digit]
        for letter in letters:
            currentMnemonics[idx] = letter
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
