"""
4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis

word
l10n
i18n
p43s

"""
for _ in range((int(input()))):
    a = input()
    if len(a) <= 10:
        print(a)
    else:
        print(a[0]+str(len(a)-2)+a[-1])
