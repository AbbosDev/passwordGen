#################################################
#   Author:     Abbas Al-Akashi                 #
#   Date:       03/20/2020                      #
#   Descr:      Making a password generator     #
#################################################

####################################################
# fix some bugs such as:
#   if all checks are checked then output error
#   clear the previous output for password
#   if text box doesn't have value then output error
####################################################


import string
import random
import tkinter as tk

#string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#string.digits = '0123456789'
#string.punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
listPunc = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '?', '@', '{', '}', '|', '~']


def randLetter():
	random_letter = random.choice(list(string.ascii_letters))	
	return random_letter

def randNum():
	random_num = random.choice(list(string.digits))
	return random_num

def randPunc():
	random_punc = random.choice(listPunc)
	return random_punc

def randFunc(randList):
	random_func = random.choice(randList)
	return random_func

def main():
    #initializing
    passLabel = tk.Label(text="").grid(row=10,column=0)

    #have it where if no value is inputed
    amt = int(e1.get())

    FuncList = []
    
    #maybe use a switch so that the default is nothing checked
    if(lVar.get() == 0):
        FuncList.append('randLetter')
    if(nVar.get() == 0):
        FuncList.append('randNum')
    if(pVar.get() == 0):
        FuncList.append('randPunc')

    passList = []

    for i in range(amt):
        wchFunc = randFunc(FuncList)
        if(wchFunc == 'randLetter'):
            password = randLetter()
        elif(wchFunc == 'randNum'):
            password = randNum()
        elif(wchFunc == 'randPunc'):
            password = randPunc()
        passList.append(password)
	
    yourPass = ''.join(passList)
    
    #clear the previous password
    #show the user the password
    passLabel = tk.Label(text='Your Password: ' + yourPass, width=(int(e1.get()) + 15))
    passLabel.grid(row=5,column=1)
   

m = tk.Tk()

#window title
m.title('Abbas Pass Gen')

#makes a button when you press it it runs the main function
tk.Button(m, text='Generate', width = 15, command=main).grid(row=5)

#check what is valid
#ex: randNum, randPunc, or randLetter
tk.Label(m, text='What is valid: ').grid(row=0,column=0)
lVar = tk.IntVar()
tk.Checkbutton(m, text='Letter', variable=lVar).grid(row=1,column=1)
nVar = tk.IntVar()
tk.Checkbutton(m, text='Number', variable=nVar).grid(row=2,column=1)
pVar = tk.IntVar()
tk.Checkbutton(m, text='Punc', variable=pVar).grid(row=3,column=1)

#get the value of how long they want the password
tk.Label(m, text='Length: ').grid(row=4)
e1 = tk.Entry(m)
e1.grid(row=4, column=1)

#close the window
tk.Button(m, text='Close', width=15, command=m.destroy).grid(row=6)

#continue showing window
m.mainloop()
