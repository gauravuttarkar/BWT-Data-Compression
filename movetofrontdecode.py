def mtfdecode(wordcode):
	# alphalist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
	# 			 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
	# 			 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8',
	# 			 '9', '0', ' ', '/', '?', '#', '.', ',', ';', '{', '}', '[', ']', '+', '-', '_', ')', '.', '(', '@',
	# 			 '!', '`', '&', '*', '%', '$', ':', ' ', '\n', chr(39),chr(34), chr(9), chr(8221), chr(8212), chr(8220),
	# 			 chr(8217), chr(8216)]
	alphalist = []
	for i in range(65535):
		alphalist.append(chr(i))
	outputarr=[]
	for i in range(len(wordcode)):
		outputarr.append(alphalist[wordcode[i]])
		del alphalist[wordcode[i]]
		alphalist.insert(0,outputarr[i])
	return outputarr	


