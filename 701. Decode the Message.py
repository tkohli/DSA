key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
i = ord("a")
dct = {}
for ch in key:
    if i == ord("z")+1:
        break
    if ch in dct or ch == " ":
        continue
    dct[ch] = chr(i)
    i += 1
ans = ""
for ch in message:
    if ch == " ":
        ans += " "
    else:
        ans += dct[ch]
print(ans)
