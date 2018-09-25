while True:
	a=input("enter d to roll the dice")
	if(a=="d"):
		import random
		r=random.randint(1,6)
		print(r)
	else:
		print("bye")
		break