print("hii and welcome to the game")
a=input("enter your choice rock paper scissor")
player=0
computer=0
while(player<=3 or computer<=3):
	import random
	d=['rock','paper','scissor']
	s=random.choice(d)
	print("the choice of computer is",s)
	if(a=='rock' and s=='rock' ):
		print ("its a tie")
		print("your score is",player)
		print("computer score is",computer)
		player=player
		computer=computer
		break
	elif(a=='rock' and s=='paper'):
		print("you losee")
		print("your score is",player)
		print("computer score is",computer)
		player=player
		computer=computer+1
	elif(a=='rock'and s=='scissor'):
		print("you won")
		print("your score is",player)
		print("computer score is",computer)
		player=player+1
		computer=computer
	elif(a=='paper' and s=='rock'):
		print("you won")
		print("your score is",player)
		print("computer score is",computer)
		player=player+1
		computer=computer
	elif(a=='paper' and s=='paper'):
		print("its a tie")
		print("your score is",player)
		print("computer score is",computer)
		player=player
		computer=computer
	elif(a=='paper' and s=='scissor'):
		print("you losee")
		print("your score is",player)
		print("computer score is",computer)
		player=player
		computer=computer+1
	elif(a=='scissor' and s=='rock'):
		print("you losee")
		print("your score is",player)
		print("computer score is",computer)
		player=player
		computer=computer+1
	elif(a=='scissor' and s=='paper'):
		print("you won")
		print("your score is",palyer)
		print("computer score is",computer)
		player=player+1
		computer=computer
	elif(a=='scissor' and s=='scissor'):
		print("its a tie")
		print("your score is",player)
		print("computer score is",computer)
		player=player
		computer=computer
	else:
		break