import sys
import getpass
import os

users = list()
passes = list()
names = list()

def dataInit():
	file = open("data.csv", "r")
	for x in file:
		stream = x.split(",")
		users.append(stream[0])
		passes.append(stream[1])
		names.append(stream[2])

def checkInput(user, pas):
	searchIndex = 0
	for x in users:
		if x == user:
			if pas == passes[searchIndex]: # Password verification
				return 1, names[searchIndex] # User found, also returns name of user
			else:
				return 2, 0
				continue
		else:
			searchIndex += 1
			continue

def verifyUser(user):
	usercount = users.count(user)
	if usercount < 1:
		return False #Username not found
	else:
		return True

if __name__ == "__main__":
	dataInit()
	print ("Please log in.")
	print ("Username: ", end = '')
	userInput = input()
	while userInput == "":
		print ("You have not entered a username, please try again: ", end = '')
		userInput = input()
	checkUser = verifyUser (userInput)
	if checkUser:
		passInput = getpass.getpass()
		while passInput == "":
			passInput = getpass.getpass("No password entered, please try again: ")
		checkFlag, name = checkInput (userInput, passInput)
		if checkFlag == 1:
			os.system('clear')
			print ("Successful login. Welcome",name)
		elif checkFlag == 2:
			while checkFlag == 2:
				passInput = getpass.getpass("Wrong password, please try again: ")
				checkFlag, name = checkInput (userInput, passInput)
			os.system('clear')
			print ("Successful login. Welcome",name)
	else:
		print ("Username does not exist.")