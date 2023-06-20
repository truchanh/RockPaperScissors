"""
simple rock, paper, scrissors
"""
import random as rd

choices = ['rock', 'paper', 'scissors']

# there are many ways to get input from the user
# I have defined both function that works perfectly!
def get_user_input1():
	"""first approach"""
	while 1:
		uc = int(input('Enter:\n\t1. for rock\n\t2. for paper\n\t3. for scissors\n> '))
		if uc in (1, 2, 3): break
		else: continue
	return choices[uc-1]


def get_user_input2():
	"""second approach"""
	while 1:
		uc = input('Enter:\n\tr. for rock\n\tp. for paper\n\ts. for scissors\n> ')
		for choice in choices:
			if choice.startswith(uc.lower()): 
				return choice
			else: continue


def get_comp_input():
	cc = rd.randint(0,2)
	return choices[cc]


def determine_winner(uc, cc):
	if uc == cc: return None
	elif uc == 'rock' and cc == 'scissors' or\
	     uc == 'paper' and cc == 'rock' or\
	     uc == 'scissors' and cc == 'paper':
		return 1
	else: return 0


def main():
	uc = get_user_input2()  # get user choice
	cc = get_comp_input()  # get computer choice
	print('='*30)
	print(f'You choose: {uc}')
	print(f'Conputer choose: {cc}')
	print('='*30)
	rs = determine_winner(uc, cc)
	if rs is not None:  # can be either 1 or 0
		if rs: print('You win.')  # return 1
		else: print('You lose:(')  # return 0
	else:  # return None
		print('There\'s a tie!')


if __name__ == '__main__':
	main()
