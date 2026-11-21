import random

import prompt

MAX_NUMBER = 1000
MIN_NUMBER = 1
ROUND_COUNTS = 3


def welcome_user():
	name = prompt.string('May I have your name? ')
	print(f'Hello, {name}!')
	return name


def show_rules():
	print('Answer "yes" if the number is even, otherwise answer "no".')


def generate_number():
	return random.randint(MIN_NUMBER, MAX_NUMBER)  # ruff: ignore[suspicious-non-cryptographic-random-usage]


def get_user_answer(num):
	print(f'Question: {num}')
	return prompt.string('Your answer: ')


def is_even(num):
	return num % 2 == 0


def play_round():
	num = generate_number()
	correct_answer = 'yes' if is_even(num) else 'no'
	user_answer = get_user_answer(num)

	if user_answer == correct_answer:
		print('Correct!')
		return True
	else:
		print(
			f"'{user_answer}' is wrong answer ;(. "
			f"Correct answer was '{correct_answer}'."
		)
		return False


def play_game():
	print('Welcome to the Brain Games!')
	name = welcome_user()
	show_rules()

	for _ in range(ROUND_COUNTS):
		result = play_round()

		if not result:
			print(f'Let\'s try again, {name}!')
			break
	else:
		print(f'Congratulations, {name}!')


def main():
	play_game()


if __name__ == '__main__':
	main()	
