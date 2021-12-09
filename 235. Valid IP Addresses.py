def validIPAddresses(string):
    validIPAddress = []

    for i in range(1, min(len(string), 4)):
        currentIPAddressParts = ['', '', '', '']

        currentIPAddressParts[0] = string[:i]
        if not isValidPart(currentIPAddressParts[0]):
            continue

        for j in range(i+1, i+min(len(string)-i, 4)):
            currentIPAddressParts[1] = string[i:j]
            if not isValidPart(currentIPAddressParts[1]):
                continue

            for k in range(j+1, j+min(len(string)-j, 4)):
                currentIPAddressParts[2] = string[j:k]
                currentIPAddressParts[3] = string[k:]

                if isValidPart(currentIPAddressParts[2]) and isValidPart(currentIPAddressParts[3]):
                    validIPAddress.append(".".join(currentIPAddressParts))
    return validIPAddress


def isValidPart(string):
    IPPart = int(string)
    if IPPart > 255:
        return False
    return len(string) == len(str(IPPart))
