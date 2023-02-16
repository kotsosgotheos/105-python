# Athanasios Papapostolou, AM: 4147

import random
import platform
import os
import time

# Constants
_BANNER = """BATTLESHIP GAME
The objective is to sink the opponent's ships before the opponent sinks yours.""";
_PL = "  P1       P2";
_COLS = " 12345    12345";
_TRY_AGAIN = "Invalid position, or position already taken. Try Again: ";
_ATTACK_AGAIN = "Invalid position, or missile already thrown there. Try Again: ";
_PLAYER1SHIPS = "Player 1 enter the position of your ship no ";
_PLAYER2SHIPS = "Player 2 enter the position of your ship no ";
_GETPLAYERS = "Input 1 for 1-player game or 2 for 2-player game: ";
_PLAYER1WINS = "GAME OVER. Player 1 wins";
_PLAYER2WINS = "GAME OVER. Player 2 wins";
_CPUWINS = "GAME OVER. CPU wins";
_PLAYER1ATTACK = "Player 1 enter the position to throw the missile: ";
_PLAYER2ATTACK = "Player 2 enter the position to throw the missile: ";
_TARGETHIT = "Target hit!";
_TARGETMISSED = "Target missed!";
_PLAYER1FIRST = "Player 1 starts first";
_PLAYER2FIRST = "Player 2 starts first";
_CPUFIRST = "CPU starts first";

###
#	@func: print_dial
#	@desc: Prints the game interface
#	@param: rows -> The row list carrying info about the ships
###
def print_dial(rows):
	print(_PL);
	print(_COLS);
	# Print each row
	for i in range(5):
		print("".join(rows[i]));
	return;

###
#	@func: clear
#	@desc: Cross platform way to clear the term screen
###
def clear():
	if(platform.system() == "Windows"):
		os.system("cls"); # Windows
	else:
		os.system("clear"); # *nix systems and maybe OSX
	return;

###
#	@func: update
#	@desc: Updates the dial of the game
#	@param: rows -> The rows of the dial
#	@param: position -> The position of the missile hit
#	@param: res -> 'x' or 'o' signaling if the missile hit or not
#	@param: margin -> A boolean signaling the margin for the string formatting
#	@return: The updated rows
###
def update(rows, position, res, margin):
	if(margin):
		# Convert the letter to a number ('a' = 1, 'b' = 2, and so on)
		rows[ord(position[0]) - 97][int(position[1]) + 9] = res; # +9 for updating the second part of the list
	else:
		rows[ord(position[0]) - 97][int(position[1])] = res;
	print_dial(rows);
	return(rows);

###
#	@func: get_players
#	@desc: Checks for a valid number of players
#	@param: first -> The player chosen randomly to start first
#	@return: The number of players in the game
###
def get_players(first):
	try:
		clear();
		print(_BANNER);
		num = input(_GETPLAYERS);
		try:
			if(len(num) != 1 or int(num) < 1 or int(num) > 2):
				return(get_players(first));
			startsfirst = list(map(lambda x: _PLAYER1FIRST if first == 1 else _CPUFIRST if int(num) == 1 else _PLAYER2FIRST, [""]))[0];
			return(int(num), startsfirst);
		except ValueError as e:
			return(get_players(first));
	except RuntimeError as e:
		exit(1); # Terminate the program

###
#	@func: get_ships
#	@desc: Sets values for humans and CPU players accordingly
#	@param: players -> Determines if its a CPU or a multiplayer game
#	@return: The two lists that were created
###
def get_ships(players):
	ships_list1 = []; c1 = 0;
	ships_list2 = []; c2 = 0;

	def first_ships(ships_list1, c1):
		if c1 == 5:
			return ships_list1;
		# Grab the first players positions
		position = generate_position(1, ships_list1, _PLAYER1SHIPS + "%d: " %(c1 + 1));
		ships_list1.append(position);
		return first_ships(ships_list1, c1 + 1);

	ships_list1 = list(map(lambda x: first_ships(ships_list1, c1), [[]]))[0];

	clear();

	def second_ships(ships_list2, c2):
		if c2 == 5:
			return ships_list2;
		if(players == 1):
			# Grab the CPU's position
			position = generate_cpu_position(ships_list2);
			ships_list2.append(position);
		else: # We have checked for an invalid number of players before calling this function
			# Grab the second player's position
			position = generate_position(2, ships_list2, _PLAYER2SHIPS + "%d: " %(c2 + 1));
			ships_list2.append(position);
		return second_ships(ships_list2, c2 + 1);

	ships_list2 = list(map(lambda x: second_ships(ships_list2, c2), [[]]))[0];

	clear();
	return(ships_list1, ships_list2);

###
#	@func: generate_position
#	@desc: Ship initializer for human players (Makes sure it returns a valid position using recursive function calls)
#	@param: num -> Player number
#	@param: ships_list -> The list of ships (for error handling)
#	@param: message -> Game specific messages
#	@param: phase -> Optional variable signaling the attacking phase
#	@return: The valid position of the ships in the dial
###
def generate_position(num, ships_list, message, phase = False):
	try:
		position = input(message);
		# Caring for invalid options such as "f2", "f6", "a8", "c12"..
		try:
			if((position in ships_list) or (len(position) > 2) or (len(position) < 2) or (position[0] < 'a') or (position[0] > 'e') or (position[1] < '1') or (position[1] > '5')):
				if(phase): # Attacking phase
					# Redoes the loop recursively
					return(generate_position(num, ships_list, _ATTACK_AGAIN, phase));
				else: # Setup phase
					return(generate_position(num, ships_list, _TRY_AGAIN, phase));
			else:
				return(position); # Returns the valid position
		except IndexError as e: # Catches the IndexError
			# Redoes the iteration recursively
			if(phase): # Attacking phase
				return(generate_position(num, ships_list, _ATTACK_AGAIN, phase));
			else:
				return(generate_position(num, ships_list, _TRY_AGAIN, phase));
	except RuntimeError as e:
		exit(1); # Terminate the program

###
#	@func: generate_cpu_position
#	@desc: Ship initializer of a CPU player (Makes sure it returns a valid position using recursive function calls)
#	@param: ships_list -> The list of ships (for error handling)
#	@return: The valid position of the ships in the dial
###
def generate_cpu_position(ships_list):
	time.sleep(0.01); # Sleep for some time for the rand function to work properly
	pos = random.choice("abcde") + str(random.randint(1, 5)); # Choose a random letter and a random integer, and convert to string
	if(pos in ships_list):
		return(generate_cpu_position(ships_list)); # Redo the iteration recursively
	else:
		return(pos); # Return the valid position

###
#	@func: attack
#	@desc: The main loop of the game
#	@state["param"]: first -> Indicates the player that starts first
#	@state["param"]: players -> Indicates if we are playing a CPU of multiplayer game
#	@state["param"]: taken1 -> The positions already attacked by player 1
#	@state["param"]: taken2 -> The positions already attacked by player 2
#	@state["param"]: counter1 -> The number of ships alive for player 1
#	@state["param"]: counter2 -> The number of ships alive for player 2
#	@state["param"]: ships -> The actual positions of ships for each player
#	@state["param"]: rows -> The game dial
#	@return: The winner of the game in a string
###
def attack(state):
	def first_player(state):
		# First player
		position = generate_position(1, state["taken1"], _PLAYER1ATTACK, True);
		print("Missile thrown at: %s" %(position));
		state["taken1"].append(position); # Append to taken

		if(position in state["ships"][1]):
			state["rows"] = update(state["rows"], position, 'o', True); # Update if hit
			print(_TARGETHIT);
			state["counter1"] -= 1; # Fix the counter
		else:
			state["rows"] = update(state["rows"], position, 'x', True); # Update if not hit
			print(_TARGETMISSED);
		return(state["counter1"]);

	def second_player(state):
		# Second player
		if(state["players"] == 1):
			position = generate_cpu_position(state["taken2"]); # Generate a position randomly
		else:
			# For multiplayer we input the positions accordingly
			position = generate_position(2, state["taken2"], _PLAYER2ATTACK, True);
		print("Missile thrown at: %s" %(position));
		state["taken2"].append(position); # Append to taken
		if(position in state["ships"][0]):
			rows = update(state["rows"], position, 'o', False); # Update if hit
			print(_TARGETHIT);
			state["counter2"] -= 1; # Fix the counter
		else:
			rows = update(state["rows"], position, 'x', False); # Update if not hit
			print(_TARGETMISSED);
		return(state["counter2"]);

	try:
		# Redundant way
		if(state["first"] == 1): # If player 1 starts first
			state["counter1"] = first_player(state);
			if(not state["counter1"]): # Check if all ships are hit
				return(_PLAYER1WINS); # Return if the winner

			state["counter2"] = second_player(state);
			if(not state["counter2"]): # Check if all ships are hit
				if(state["players"] == 1):
					return(_CPUWINS); # For CPU
				else:
					return(_PLAYER2WINS); # For the second player

		else: # first == 2
			state["counter2"] = second_player(state);
			if(not state["counter2"]): # Check if all ships are hit
				if(state["players"] == 1):
					return(_CPUWINS); # For CPU
				else:
					return(_PLAYER2WINS); # For the second player

			state["counter1"] = first_player(state);
			if(not state["counter1"]): # Check if all ships are hit
				return(_PLAYER1WINS); # Return if the winner

		return(attack(state)); # Redo the loop recursively
	except RuntimeError as e: # Quick bypass of the recursion depth errors
		exit(1); # Terminate the program

###
#	@func: main
###
def main():
	# Create the row lists (Easier to manipulate that strings)
	r1 = ['a', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'a', ' ', ' ', ' ', ' ', ' ', ' '];
	r2 = ['b', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'b', ' ', ' ', ' ', ' ', ' ', ' '];
	r3 = ['c', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'c', ' ', ' ', ' ', ' ', ' ', ' '];
	r4 = ['d', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' '];
	r5 = ['e', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'e', ' ', ' ', ' ', ' ', ' ', ' '];
	rows = [r1, r2, r3, r4, r5]; # Create the dynamic rows

	# Choose who starts randomly
	first = list(map(lambda x: random.choice([1, 2]), [0]))[0];

	# Makes sure it returns a valid numebr of players
	players, startsfirst = get_players(first);

	# Gets the positions of the ships
	ships = list(map(lambda x: get_ships(1) if players == 1 else get_ships(2), [[]]))[0];

	#print(ships); # DEBUG #

	# Prints the winner of the game
	state = {"first": first, "players": players, "taken1": [], "taken2": [], "counter1": 5, "counter2": 5, "ships": ships, "rows": rows};
	print(startsfirst);
	print(attack(state));
	return;

if(__name__ == "__main__"):
	main();
