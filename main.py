# to shuffle the deck
import random
# to exit game
from sys import exit

ranks = [
	'Two', 
	'Three', 
	'Four', 
	'Five', 
	'Six', 
	'Seven', 
	'Eight', 
	'Nine', 
	'Ten', 
	'Jack', 
	'Queen', 
	'King', 
	'Ace'
]

suits = [
	'Hearts', 
	'Diamonds', 
	'Spades', 
	'Clubs'
]

values = {
	'Two':2, 
	'Three':3, 
	'Four':4, 
	'Five':5, 
	'Six':6, 
	'Seven':7, 
	'Eight':8, 
    	'Nine':9, 
	'Ten':10, 
	'Jack':11, 
	'Queen':12, 
	'King':13, 
	'Ace':14
}

class Card():
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(self):
		return f'{self.rank} of {self.suit}'

class Deck():
	def __init__(self):
		self.all_cards = []

		for rank in ranks:
			for suit in suits:
				self.all_cards.append(Card(suit, rank))

	def shuffle_deck(self):
		random.shuffle(self.all_cards)

	def deal_one(self):
		return self.all_cards.pop()

class Player():
	def __init__(self, name):
		self.name = name
		self.player_cards = [] # holds the cards distributed to the player 

	def add_cards(self, new_cards):
		if isinstance(new_cards, list):
			self.player_cards.extend(new_cards)
		else:
			self.player_cards.append(new_cards)

	def remove_card(self):
		return self.player_cards.pop(0)

	def __str__(self):
		return f"{self.name} has {len(self.player_cards)} cards"

# game setup

# variables
name1 = ''
name2 = ''
game_on = True
round_num = 0

# validating name input
while name1 == '' or name2 == '':
	name1 = input('Enter the name of first player: ')
	name2 = input('Enter the name of second player: ')

# creating an instance of two players
player1 = Player(name1)
player2 = Player(name2)

# creating an instance deck 
deck = Deck()
deck.shuffle_deck()

# distributing cards equally amongst players
for x in range(26):
	player1.add_cards(deck.deal_one())
	player2.add_cards(deck.deal_one())

# initializing game
while game_on:
	round_num += 1
	print(f'Round {round_num}')

	# check for players out of cards
	if len(player1.player_cards) == 0:
		print(f'\n{player1.name} out of cards\n{player2.name} wins!')
	elif len(player2.player_cards) == 0:
		print(f'\n{player2.name} out of cards\n{player1.name} wins!')

	# cards of players on table
	player1_cards = []
	player2_cards = []

	# dealing player cards on table
	try:
		player1_cards.append(player1.remove_card())
		player2_cards.append(player2.remove_card())
	except IndexError:
		pass

	#while at_war
	at_war = True

	while at_war:
		try:
			if player1_cards[-1].value > player2_cards[-1].value:
				# player 1 wins the cards
				player1.add_cards(player1_cards)
				player1.add_cards(player2_cards)

				print(f'{player1.name} wins round {round_num}!\n')

				at_war = False
			elif player2_cards[-1].value > player1_cards[-1].value:
				# player 2 wins the cards
				player2.add_cards(player2_cards)
				player2.add_cards(player1_cards)

				print(f'{player2.name} wins round {round_num}!\n')

				at_war = False

			else:
				print('WAR!')
				# check for enough cards

				if len(player1.player_cards) < 5:
					print(
						f"\n{player1.name} doesn't have enough cards to declare war\n{player2.name} wins!"
						)
					game_on = False
					exit('\nGame Over')
				elif len(player2.player_cards) < 5:
					print(
						f"\n{player2.name} doesn't have enough cards to declare war\n{player1.name} wins!"
					)
					game_on = False
					exit('\nGame Over')

				# if value of cards of both players are equal:
					# war continues 
				else:
					for x in range(5):
						player1_cards.append(player1.remove_card())
						player2_cards.append(player2.remove_card())

		except IndexError:
			exit('\nGame Over')
