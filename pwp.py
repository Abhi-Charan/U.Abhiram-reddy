print("Hi.....!!!! Welcome to Secret Message Portal..<3")
print("we have options for you:")
print("Simple coding-c")
print("Simple Decoding-d")
print("Name Fun-n")
print("Funny Msg-f")
print("Letter-l")
l=input("choose your option-")


def code():
	alpha="abcdefghijklmnopqrstuvwxyz"
	key=3
	newmsg=''
	msg=input("enter the message you want to convert...  ")
	for character in msg:
		if character in alpha:
			posi=alpha.find(character)
			nposi=(posi+key)%26
			newcar=alpha[nposi]
			newmsg +=newcar
		else:
			newmsg +=character
	print("your converted message is-")
	print(newmsg)
def decode():
	alpha="abcdefghijklmnopqrstuvwxyz"
	key=3
	newmsg=''
	print("I see you got a weird text...Let me fix it for you :)")
	msg=input("enter the weird message you recieved...")
	for character in msg:
		if character in alpha:
			posi=alpha.find(character)
			nposi=(posi-key)%26
			newcar=alpha[nposi]
			newmsg +=newcar
		else:
			newmsg +=character
	print("the weird message was-")
	print(newmsg)
def name():
	alpha="abcdefghijklmnopqrstuvwxyz"
	key=3
	newmsg=''
	msg=input("enter your name...^_^")
	for character in msg:
		if character in alpha:
			posi=alpha.find(character)
			nposi=(posi+key)%26
			newcar=alpha[nposi]
			newmsg +=newcar
		else:
			newmsg +=character
	print("Your converted name is-")
	print(newmsg)
def letter():
	alpha="abcdefghijklmnopqrstuvwxyz"
	key=3
	newmsg=''
	print("Oh My God...!!!! you got a letter XD")
	msg=input("enter the message which is written for you...!")
	for character in msg:
		if character in alpha:
			posi=alpha.find(character)
			nposi=(posi+key)%26
			newcar=alpha[nposi]
			newmsg +=newcar
		else:
			newmsg +=character
	print("The Letter said.....")
	print(newmsg)
	print("....")
def fun():
	alpha="abcdefghijklmnopqrstuvwxyz"
	key=3
	newmsg=''
	msg=input("enter the funny text..")
	for character in msg:
		if character in alpha:
			posi=alpha.find(character)
			nposi=(posi+key)%26
			newcar=alpha[nposi]
			newmsg +=newcar
		else:
			newmsg +=character
	print("the funny converted message is..|")
	print(newmsg)
	print("Have fun messing around with your friends.. ^_^")


if(l=='c'):
	code()
elif(l=='d'):
	decode()
elif(l=='n'):
	name()
elif(l=='l'):
	letter()
elif(l=='f'):
	fun()
else:
	print("wrong key")
	exit()
