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
	usercount = users.count(user)
	if usercount < 1:
		return 0, 0  #Username not found
	searchIndex = 0
	for x in users:
		if usercount > 0:
			if x == user:
				if pas == passes[searchIndex]:
					return 1, names[searchIndex] # User found, also returns name of user
				else:
					searchIndex += 1
					continue
			else:
				searchIndex += 1
				continue
		else:
			return 0, 0


if __name__ == "__main__":
	dataInit()
	print ("Please log in.")
	print ("Username: ", end = '')
	userInput = input()
	passInput = getpass.getpass()
	checkFlag, name = checkInput (userInput, passInput)
	if checkFlag == 0:
		print ("User not found.")
	elif checkFlag == 1:
		os.system('clear')
		print ("Successful login. Welcome %s!" % name)