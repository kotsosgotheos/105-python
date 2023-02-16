# Athanasios Papapostolou, AM: 4147

import random
import platform
import os
import time

# Constant variables
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
#	@closure: generate_single_position
#	@desc: Executes the appropriate function according to the number of players
#	@return: The valid position
###
generate_single_position = lambda func, it, *args: func(args[0], args[1], args[2] + "%d: " %(it + 1), args[3]);

###
#	@closure: generate_ships
#	@desc: Executes the appropriate function according to the number of players
#	@return: The list of ships yielded by the generators
###
generate_ships = lambda func, *args: [generate_single_position(func, it, *args) for it in range(5)];

###
#	@func: print_dial
#	@desc: Prints the game interface
#	@param: rows -> The row list carrying info about the ships
###
def print_dial(rows):
	print(_PL);
	print(_COLS);
	# Print each row
	for item in rows:
		print("".join(item));
	return;

###
#	@func: clear
#	@desc: Cross platform way to clear the term screen
###
def clear():
	os.system("cls") if platform.system() == "Windows" else os.system("clear"); # *nix systems and maybe OSX
	return;

###
#	@func: update
#	@desc: Updates the dial of the game
#	@param: rows -> The rows of the dial
#	@param: position -> The position of the missile hit
#	@param: res -> 'x' or 'o' signaling if the missile hit or not
#	@param: margin -> A integer signaling the margin for the string formatting
#	@return: The updated rows
###
def update(rows, position, res, margin = 0):
	# Convert the letter to a number ('a' = 1, 'b' = 2, and so on)
	rows[ord(position[0]) - 97][int(position[1]) + margin] = res; # +margin for updating the second part of the list
	print_dial(rows); # Prints the updated dial
	return(rows); # Returns the updated rows

###
#	@func: get_players
#	@desc: Checks for a valid number of players
#	@param: first -> The player chosen randomly to start first
#	@return: The number of players in the game
###
def get_players(first):
	try:
		clear();
		num = input(_BANNER + "\n" + _GETPLAYERS);
		return get_players(first) if num not in ["1", "2"] else int(num);
	except RuntimeError as e:
		exit(1); # Terminate the program

###
#	@func: get_ships
#	@desc: Sets values for humans and CPU players accordingly
#	@param: players -> Determines if its a CPU or a multiplayer game
#	@return: The two lists that were created
###
def get_ships(players):	
	ships_list1 = generate_ships(generate_position, 1, [], _PLAYER1SHIPS, False);
	clear(); # Grab the first players positions
	ships_list2 = generate_ships(generate_cpu_position, "", [], "", "") if players == 1 else generate_ships(generate_position, 2, [], _PLAYER2SHIPS, False);
	clear(); # Grab the second player's position
	return(ships_list1, ships_list2); # Return the two lists

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
	# Redoes the iteration recursively according to the game phase
	recall = lambda num, ships_list, message, phase = False: generate_position(num, ships_list, _ATTACK_AGAIN, phase) if phase else generate_position(num, ships_list, _TRY_AGAIN, phase);

	try:
		pos = input(message); # Get a position
		# Caring for invalid options such as "f2", "f6", "a8", "c12"..
		if pos in ships_list or len(pos) != 2 or pos[0] not in ['a','b','c','d','e'] or pos[1] not in ['1','2','3','4','5']:
			return recall(num, ships_list, message, phase);
		else:
			ships_list.append(pos);
			return(pos); # Returns the valid position
	except RuntimeError as e:
		exit(1); # Terminate the program

###
#	@func: generate_cpu_position
#	@desc: Ship initializer of a CPU player (Makes sure it returns a valid position using recursive function calls)
#	@param: ships_list -> The list of ships (for error handling)
#	@param: dummy1, dummy2 -> Two dummy variables for the purpose of lazy polymorphism in closures
#	@return: The valid position of the ships in the dial
###
def generate_cpu_position(dummy1, ships_list, dummy2, dummy3 = False):
	time.sleep(0.01); # Sleep for some time for the rand function to work properly
	pos = random.choice("abcde") + str(random.randint(1, 5)); # Choose a random letter and a random integer, and convert to string
	def ret_pos(pos):
		ships_list.append(pos);
		return pos;
	return generate_cpu_position(dummy1, ships_list, dummy2, dummy3) if pos in ships_list else ret_pos(pos); # Redo the iteration recursively

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
	p1 = lambda state, *args: _PLAYER1WINS if not player_attack(state, args[0], args[1], args[2]) else False; # Check if all ships are hit and return the winner
	p_cpu = lambda state: _CPUWINS if state["players"] == 1 else _PLAYER2WINS; # Inner conditional
	p2 = lambda state, *args: p_cpu(state) if not player_attack(state, args[0], args[1], args[2]) else False; # Same for player 2 (or CPU)

	# Closures keep the 'state' variable in a in-function global scope
	def player_attack(state, p, cpu, margin): # p -> "1" or "2", cpu -> True or False, margin -> 0 or 9
		def hit(state, position):
			state["rows"] = update(state["rows"], position, 'o', margin); # Update if hit
			print(_TARGETHIT);
			state["counter"+p] -= 1; # Fix the counter

		def not_hit(state, position):
			state["rows"] = update(state["rows"], position, 'x', margin); # Update if not hit
			print(_TARGETMISSED);

		# For a cpu player
		if state["players"] == 1 and cpu == True:
			position = generate_cpu_position(int(p), state["taken"+p], eval("_PLAYER"+p+"ATTACK"), True); # Generate a position randomly
		else:
			# For multiplayer we input the positions accordingly
			position = generate_position(int(p), state["taken"+p], eval("_PLAYER"+p+"ATTACK"), True);

		print("Missile thrown at: %s" %(position));
		state["taken"+p].append(position); # Append to taken
		hit(state, position) if position in state["ships"][2 - int(p)] else not_hit(state, position);
		return state["counter"+p];

	try:
		if state["first"] == 1: # If player 1 starts first
			winner1 = p1(state, "1", False, 9); # Check if all ships are hit
			if winner1:
				return winner1; # Return if the winner
			winner2 = p2(state, "2", True, 0); # Check if all ships are hit
			if winner2:
				return winner2 # Return if the winner
		else: # first == 2
			winner2 = p2(state, "2", True, 0); # Check if all ships are hit
			if winner2:
				return winner2; # Return if the winner
			winner1 = p1(state, "1", False, 9); # Check if all ships are hit
			if winner1:
				return winner1; # Return if the winner
		return attack(state); # Redo the loop recursively
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
	first = random.choice([1, 2]);

	# Makes sure it returns a valid numebr of players
	players = get_players(first);

	# Gets the positions of the ships
	ships = get_ships(1) if players == 1 else get_ships(2); # Returns immutable data

	# print(ships); # DEBUG #

	# Prints the winner of the game
	state = {"first": first, "players": players, "taken1": [], "taken2": [], "counter1": 5, "counter2": 5, "ships": ships, "rows": rows};
	print(_PLAYER1FIRST if first == 1 else _CPUFIRST if players == 1 else _PLAYER2FIRST);
	print_dial(rows);
	print(attack(state));
	return;

if(__name__ == "__main__"):
	main();
