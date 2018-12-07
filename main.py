distanceFromBorder = 2

def contents(fileName):
	result = []
	with open(fileName, 'r') as text:
		for line in text:
			result.append(line)
	return result

def printLine(lenght):
	print("+", end = "")
	for i in range(lenght - 2):
		print("-", end = "")
	print("+")


def findMaximumLenght(allInput, numberOfSubjects):
	result = [0] * numberOfSubjects

	for index in range(len(allInput)):
		info = allInput[index].split(",")

		for subject in range(numberOfSubjects):
			result[subject] = max(result[subject], len(info[subject]))

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

def printInfo(info, lenghtSubjects, numberOfSubjects):
	for index in range(numberOfSubjects):
		print("|", end = "")

		beginSpace = (lenghtSubjects[index] - len(info[index])) // 2
		endSpace = (lenghtSubjects[index] - len(info[index])) - beginSpace
		
		printSpaces(beginSpace)
		print(info[index], end = "")
		printSpaces(endSpace)
	print("|")

def printRes(allInput, lenghtSubjects, sumLenght, numberOfSubjects):
	for info in allInput:
		infoStrip = info.strip()
		infoSplit = infoStrip.split(",")
		printLine(sumLenght)
		printInfo(infoSplit, lenghtSubjects, numberOfSubjects)
	printLine(sumLenght)


print("Enter csv path : ", end = "")
csvAddress = input()

allInput = contents(csvAddress)
subjects = allInput[0].split(",")

numberOfSubjects = len(subjects)

maxLenghtSubjects = findMaximumLenght(allInput, numberOfSubjects)

lenghtSubjects = addToMax(maxLenghtSubjects, distanceFromBorder)
sumLenght = findLenght(lenghtSubjects)

printRes(allInput, lenghtSubjects, sumLenght, numberOfSubjects)