def generateDocument(characters, document):
    dct = {}
	for c in characters:
		if c in dct:
			dct[c]+=1
		else:
			dct[c]=1
	for d in document:
		if d not in dct or dct[d]==0:
			return False
		dct[d]-=1
	return True
			
			
	