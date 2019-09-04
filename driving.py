ask = input('are you driving? ')
speed =  input('what is your speed? ')
speed = int(speed)
if ask == 'yes':
	if speed >= 55:
		print('drive safe')
	else:
		print('hurry up')
elif ask == 'no':
	print('just drive')
else:
	print('only tell me yes or no')
