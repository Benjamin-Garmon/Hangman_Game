import random
#shows the blanks for the word that was picked
def shw_wrd(blank_lst):
	return''.join(blank_lst)

with open('sowpods.txt', 'r') as file:
#creates a word list from the file. chooses one and creates a list of blanks for shw_wrd	
	wrd_lst = [i for i in file]
	rdm_wrd = random.choice(wrd_lst)
if '\n' in rdm_wrd:
	rdm_wrd_str = rdm_wrd.strip('\n')
	rdm_wrd = list(rdm_wrd_str)
blk_wrd = ['_ ' for i in rdm_wrd]

#guess list so player can see letters already chosen
guess_lst = []
# 10 chances to get the letters right
x=10 
while x>=0:
	print(shw_wrd(blk_wrd))
	print(f'***your guesses***: {guess_lst}\n')
	if x == 0:
		print('---You Lose!!!---')
		print(f'***ANSWER: {rdm_wrd_str}***')
		break
	elif shw_wrd(blk_wrd)==rdm_wrd_str:
		print('------You win!!!------')	
		break	
	else:
		while True:
			user_guess = input('give a letter guess: ')
			#all string from SOWPADS are upper case
			user_guess = user_guess.upper()
			#avoid picked letters affecting your 10 chances
			if user_guess in guess_lst:
				print('***Already Guessed... Try Again***\n')
				continue
			#if you guess wrong. show how many guesses you have left
			elif user_guess not in rdm_wrd:
				guess_lst.append(user_guess)
				print('\n***try again***')
				x-=1
				print(f'***you have {x} guesses left***\n')
				break

			else:
				guess_lst.append(user_guess)
				#get index from the random word so the blanks displayed can be changed to the user guess in the proper place
				for index, j in enumerate(rdm_wrd):
					if user_guess == j:
						blk_wrd[index]=user_guess
				break
		continue
