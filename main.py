def contents(fileName):
	result = []
	with open(fileName, 'r') as text:
		for line in text:
			result.append(line)
	return result

def proSplit(line):
	res = []
	left = 0
	right = 1
	longOne = False
	while left < len(line):
		if line[left] == '"':
			longOne = True
		while right < len(line) and ((line[right] != ',' and longOne == False) or (line[right] != '"' and longOne == True)):
			right += 1
		if longOne == True:
			res.append(line[left + 1:right])
			left = right + 2
			right = left + 1
			longOne = False
		else:
			res.append(line[left:right])
			left = right + 1
			right = left + 1
	return res


def printLine(lenght):
	print("+", end = "")
	for i in range(lenght - 2):
		print("-", end = "")
	print("+")


def findMaximumLenght(allGoodInput, numberOfSubjects):
	result = [0] * numberOfSubjects
	for info in allGoodInput:
		for subject in range(numberOfSubjects):
			for line in info[subject]:
				result[subject] = max(result[subject], len(line))
	return result

def addToMax(maxLenghtSubjects, distanceFromBorder):
	result = []
	for lenght in maxLenghtSubjects:
		result.append(lenght + distanceFromBorder * 2)
	return result

def findLenght(lenghtSubjects):
	result = 1
	for lenSubject in lenghtSubjects:
		result += lenSubject + 1
	return result

def printSpaces(number):
	for i in range(number):
		print(" ", end = "")

def printInfo(info, lenghtSubjects, numberOfSubjects, whichLine):
	for index in range(numberOfSubjects):
		print("|", end = "")
		if len(info[index]) > whichLine:
			beginSpace = (lenghtSubjects[index] - len(info[index][whichLine])) // 2
			endSpace = (lenghtSubjects[index] - len(info[index][whichLine])) - beginSpace
		
			printSpaces(beginSpace)
			print(info[index][whichLine], end = "")
			printSpaces(endSpace)
		else:
			printSpaces(lenghtSubjects[index])

	print("|")

def printRes(allGoodInput, lenghtSubjects, sumLenght, numberOfSubjects, numberOfLines):
	for i in range(len(allGoodInput)):
		printLine(sumLenght)
		for j in range(numberOfLines[i]):
			printInfo(allGoodInput[i], lenghtSubjects, numberOfSubjects, j)
	printLine(sumLenght)


def strSplit(str, maxWidth):
	res = []
	words = str.split(" ")
	past = ""
	for word in words:
		if len(past) + len(word) + 1 <= maxWidth:
			if past == "":
				past = word
			else:
				past += " " + word
		else:
			res.append(past)
			past = word
	res.append(past)
	return res

def makeData(allInput, maxWidth):
	res = []
	for info in allInput:
		res.append(proSplit(info.strip()))
	for i in range(len(res)):
		for j in range(len(res[i])):
			str = res[i][j]
			res[i][j] = strSplit(str, maxWidth)
	return res

def findNumberOfLines(allGoodInput):
	res = []
	for info in allGoodInput:
		line = 0
		for subject in info:
			line = max(line, len(subject))
		res.append(line)
	return res


print("Enter csv path : ", end = "")
csvAddress = input()
print("Enter max width : ", end = "")
maxWidth = int(input().strip())
print("Enter border width(Recommended = 2) : ", end = "")
distanceFromBorder = int(input().strip())

allInput = contents(csvAddress)
allGoodInput = makeData(allInput, maxWidth)



subjects = proSplit(allInput[0])

numberOfSubjects = len(subjects)

maxLenghtSubjects = findMaximumLenght(allGoodInput, numberOfSubjects)

lenghtSubjects = addToMax(maxLenghtSubjects, distanceFromBorder)
sumLenght = findLenght(lenghtSubjects)

numberOfLines = findNumberOfLines(allGoodInput)

printRes(allGoodInput, lenghtSubjects, sumLenght, numberOfSubjects, numberOfLines)