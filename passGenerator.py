import string
import random

#string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#string.digits = '0123456789'
#string.punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

def randLetter():
	random_letter = random.choice(list(string.ascii_letters))	
	return random_letter

def randNum():
	random_num = random.choice(list(string.digits))
	return random_num

def randPunc():
	random_punc = random.choice(list(string.punctuation))
	return random_punc

def randFunc(randList):
	random_func = random.choice(randList)
	return random_func


amt = 10

FuncList = []

FuncList.append('randLetter')
FuncList.append('randNum')
FuncList.append('randPunc')

passList = []

for i in range(amt):
	wchFunc = randFunc(FuncList)	
	if (wchFunc == 'randLetter'):
		password = randLetter()
	elif (wchFunc == 'randNum'):
		password = randNum()
	elif (wchFunc == 'randPunc'):
		password = randPunc()	
	passList.append(password)
	
yourPass = ''.join(passList)
print(yourPass)
