import random

password=int(input('enter a password : '))


for i in range(1,10000):
	ran=random.randint(0,10000)
	if( password != int(ran)):
		print (f'trying  : {ran}      times{i}')
		
	else:
		print(f"your password {ran}")
		break
	
		
			