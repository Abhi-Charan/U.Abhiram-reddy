import random
print("hiii,welcome to the game snake & ladders")
count=0
while(count<=100):
	a=input("enter d to roll the dice")
	if(a=='d'):
		r=random.randint(1,6)
		print("r value is",r)
		count=count+r
		print("Score is",count)
		if(count==100):
			print("you won")
			print("your score is",count)
		elif(count==8):
			count=37
			print("hurray you have climb up a ladder")
		elif(count==11):
			count=2
			print("oops you have a snake bite")
		elif(count==13):
			count=34
			print("hurray you have climb up a ladder")
		elif(count==38):
			count=9
			print("oops you have a snake bite")
		elif(count==40):
			count=68
			print("hurray you have climb up a ladder")
		elif(count==52):
			count=81
			print("hurray you have climb up a ladder")
		elif(count==65):
			count=46
			print("oops you have a snake bite")
		elif(count==76):
			count=97
			print("hurray you have climb up a ladder")
		elif(count==25):
			count=4
			print("oops you have a snake bite")
		elif(count==89):
			count=70
			print("oops you have a snake bite")
		elif(count==93):
			count=64
			print("oops you have a snake bite")
	else:
		break
