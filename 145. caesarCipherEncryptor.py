#caesarCipherEncryptor
def caesarCipherEncryptor(string, key):
    lst = list("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
	key = key%26
	out = []
	for s in string:
		out.append(lst[lst.index(s)+key])
	return "".join(out)
