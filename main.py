import random
import time
import re

FILE_STARTING = "starting_messages.txt"

FILE_DENIAL = "denial.txt"
FILE_ANGER = "anger.txt"
FILE_BARGAINING = "bargaining.txt"

FILE_SUPPORT = "support_messages.txt"
FILE_FAREWELLS = "farewells_messages.txt"

def getInput():
	"""
	ToDo
	Get input since:
		file
		console
		parameter
	"""
	expired_name = "beny"
	expired_genre = "m"
	condolenced_name = "daniel"
	condolenced_genre = "m"

	return {"expired_name":expired_name, "expired_genre":expired_genre, "condolenced_name":condolenced_name, "condolenced_genre":condolenced_genre}

def makeGreeting(input_data):
	#getting random numbers
	greeting_before = random.randint(0, 1) #for choosing if name goes before or after greeting
	greeting_number = random.randint(0, 3) #for choosing 1 of 4 greetings

	#getting greeting based in the number choosen
	greeting = getGreeting(greeting_number)

	#Shorters
	is_male = True if (input_data["condolenced_genre"] == "m") else False
	name = input_data["condolenced_name"]
	
	#Choosing word's sex
	if greeting_number == 3:
		greeting = wordSexualizer(greeting, input_data["condolenced_genre"])

	#setting if greeting goes after or before
	if greeting_before:
		"""
		ToDo
			fix problem with empty greeting		
		"""
		return greeting.capitalize() + " " + name.capitalize()
	else:
		return name.capitalize() + " " + greeting.casefold()

def getGreeting(number):
	#Greetings types list
	greetings = ["", "Hola", "Buen@", "Querid@"]

	#if number == Buen
	if number == 2:
		#Get actual time (computer's time)
		actual_time = time.ctime()
		#Time structure "Mon Jan 11 16:54:49 2021"
		#Time wanted structure "23:59:59"
		pattern = re.compile(r'\d\d:\d\d:\d\d')
		#Getting just hours:minutes:seconds with regex
		actual_time = pattern.findall(actual_time)[0]
		#if is at morning
		if int(actual_time[:2]) < 12:
			return greetings[2].replace('@', "os días")
		#if is at evening
		elif int(actual_time[:2]) < 19:
			return greetings[2].replace('@', "as tardes")
		else:
			return greetings[2].replace('@', "as noches")
	else:
		return greetings[number]

def wordSexualizer(word, sex):
	if sex == 'm':
		return word.replace('@', 'o')
	elif sex == 'f':
		return word.replace('@', 'a')

def getRandomLineFromFile(file_name):
	#Helpers
	file_content = [] #Stores all the lines in the file
	number_lines = 0	#Counts how many lines are int he file

	#Fancy way to open and read a file (using utf-8 because text is in spanish)
	with open(file_name, 'r', encoding="utf-8") as file:
		for line in file:
			number_lines +=1
			file_content.append(line.replace("\n", ""))

	#Getting a random number between 0 and N number of lines
	random_number = random.randint(0, number_lines-1)
	return file_content[random_number-1].casefold()

def throughThePark(files):
	#Algorithm logic: omitte some files to get "elipsis"
	ommitted = random.randint(0, len(files)-1)

	#eliminate omitted file
	files.pop(ommitted)

	#Get 1 message of every file
	messages = []
	for file in files:
		messages.append(getRandomLineFromFile(file))

	return messages


def main():
	input_data = getInput()
	print(makeGreeting(input_data))
	print(getRandomLineFromFile(FILE_STARTING))

	print(throughThePark([FILE_DENIAL, FILE_ANGER, FILE_BARGAINING]))

	print(getRandomLineFromFile(FILE_SUPPORT))
	print(getRandomLineFromFile(FILE_FAREWELLS))

	thanatology_message = ""
	thanatology_message += makeGreeting(input_data)
	thanatology_message += ", " + getRandomLineFromFile(FILE_STARTING)

	result = throughThePark([FILE_DENIAL, FILE_ANGER, FILE_BARGAINING])
	thanatology_message += ", " + result[0] + ", " + result[1]

	thanatology_message += ", " + getRandomLineFromFile(FILE_SUPPORT)
	thanatology_message += ", " + getRandomLineFromFile(FILE_FAREWELLS) + "."

	print()
	print(thanatology_message)


if __name__ == "__main__":
	main()