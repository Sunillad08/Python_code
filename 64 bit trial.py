number_of_days = 30
monday = 1
for monday in range(1,8):
	if monday > 1:
		middle = '⬛'*(7 - (monday - 1)) + '⬜'*(monday - 1)
		print(f'01 {middle} {monday-1:02} \n')
	for i in range(monday,number_of_days+1,7):
		middle = '⬜'*(min(i+6,number_of_days) - i + 1) + '⬛'*(6 - (min(i+6,number_of_days) - i))
		print(f'{i:02} {middle} {min(i+6,number_of_days):02} \n')