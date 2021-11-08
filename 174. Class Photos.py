def classPhotos(redShirtHeights, blueShirtHeights):
	redShirtHeights.sort(reverse = True)
	blueShirtHeights.sort(reverse = True)
	redFirst = redShirtHeights> blueShirtHeights
    for i,j in zip(redShirtHeights, blueShirtHeights):
		if i>j and redFirst:
			pass
		elif i<j and redFirst is False:
			pass
		else:
			return False
	return True
