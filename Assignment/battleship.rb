class Screen
	def initialize
		# Constants
		r1 = ['a', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'a', ' ', ' ', ' ', ' ', ' ', ' '];
		r2 = ['b', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'b', ' ', ' ', ' ', ' ', ' ', ' '];
		r3 = ['c', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'c', ' ', ' ', ' ', ' ', ' ', ' '];
		r4 = ['d', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' '];
		r5 = ['e', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'e', ' ', ' ', ' ', ' ', ' ', ' '];
		
		@_BANNER = "BATTLESHIP GAME\nThe objective is to sink the opponent's ships before the opponent sinks yours.";
		@_PL = "  P1       P2";
		@_COLS = " 12345    12345";
		@getPlayers = "Input 1 for 1-player game or 2 for 2-player game: ";
		@player1wins = "GAME OVER. Player 1 wins";
		@player2wins = "GAME OVER. Player 2 wins";
		@cpuWins = "GAME OVER. CPU wins";
		@targetHit = "Target hit!";
		@targetMissed = "Target missed!";
		@player1first = "Player 1 starts first";
		@player2first = "Player 2 starts first";
		@cpuFirst = "CPU starts first";
		@player1ships = "Player 1 enter the position of your ship no";
		@player2ships = "Player 2 enter the position of your ship no";
		@player1attack = "Player 1 enter the position to throw the missile: ";
		@player2atatck = "Player 2 enter the position to throw the missile: ";
		@playerAgain = "Invalid position, or position already taken. Try Again: ";
		@playerAttackAgain = "Invalid position, or missile already thrown there. Try Again: ";
		@cpuShips = "dummy";
		
		@@phase = "0"
		
		# Variables
		@num = -1;
		@first = -1;
		@ships = [];
		@ships_list1 = [];
		@ships_list2 = [];
		@dial = [r1, r2, r3, r4, r5];

		# Objects
		@human1 = nil;
		@human2 = nil;
		@cpu2 = nil;
	end

	def input(text)
		print text;
		gets.chomp;
	end

	def clear
		RUBY_PLATFORM =~ /win32|win64|\.NET|windows|cygwin|mingw32/i ? (system "cls") : (system "clear");
	end

	def print_dial
		puts(@_PL);
		puts(@_COLS);
		@dial.each do |row|
			puts row.join;
		end
	end
end

class Player < Screen
	attr_accessor :counter
	def initialize
		@counter = 5;
		super;
	end

	def generate_position(message, ships_list)
		"p2"
	end
end

class Human < Player
	def initialize
		super;
	end

	def generate_position(message, ships_list)
		position = input(message);
		if ships_list.include?(position) or position.length > 2 or position.length < 2 or position[0] < 'a' or position[0] > 'e' or position[1].to_i < 1 or position[1].to_i > 5
			if @@phase == "SET"
				generate_position(@playerAgain, ships_list);
			elsif @@phase == "ATTACK"
				generate_position(@playerAttackAgain, ships_list);
			end
		else
			ships_list << position;
			return position;
		end
	end
end

class CPU < Player
	def initialize
		super;
	end

	def generate_position(message, ships_list)
		sleep(0.01);
		position = "#{(rand 97..101).chr}#{rand 1..5}";
		if ships_list.include?(position)
			generate_position(message, ships_list);
		else
			ships_list << position;
			return position;
		end
	end
end

class Game < Screen
	def initialize
		super;
	end

	def update(position, res, margin)
		@dial[position[0].ord - 97][position[1].to_i + margin] = res;
		print_dial;
	end

	def get_players
		clear;
		puts @_BANNER;
		@num = input(@getPlayers);
		get_players if @num.length != 1 or @num.to_i > 2 or @num.to_i < 1;
		@num = @num.to_i;

		@human1 = Human.new;
		if @num == 1
			@cpu2 = CPU.new;
		else
			@human2 = Human.new;
		end
	end

	def get_ships
		@@phase = "SET";

		# First human player
		5.times do |it|
			position = @human1.generate_position("#{@player1ships} #{it + 1}: ", @ships_list1);
			@ships_list1 << position;
		end

		if @num == 1
			# Second cpu player
			5.times do |it|
				@ships_list2 << @cpu2.generate_position(@cpuShips, @ships_list2);
			end
		else
			clear;
			# Second human player
			5.times do |it|
				@ships_list2 << @human2.generate_position("#{@player2ships} #{it + 1}: ", @ships_list2);
			end
		end

		@ships << @ships_list1.uniq << @ships_list2.uniq;
		@ships_list1 = [];
		@ships_list2 = [];
		
		clear;

		@first = rand 1..2;
		puts(@player1first) if @first == 1;
		puts(@player2first) if @first == 2;
	end

	def attack
		@@phase = "ATTACK";

		if @first == 1
			first_player;
			if @human1.counter == 0
				puts(@player1wins);
				return;
			end
			
			second_player;
			if @num == 1
				if @cpu2.counter == 0
					puts(@cpuWins)
					return;
				end
			else
				if @human2.counter == 0
					puts(@player2wins);
					return;
				end
			end
		else
			second_player;
			if @num == 1
				if @cpu2.counter == 0
					puts(@cpuWins)
					return;
				end
			else
				if @human2.counter == 0
					puts(@player2wins);
					return;
				end
			end

			first_player;
			if @human1.counter == 0
				puts(@player1wins);
				return;
			end
		end
		attack;
	end

	def first_player
		position = @human1.generate_position("#{@player1attack}", @ships_list1);
		puts("Missile thrown at: #{position}");
		@ships_list1 << position;
		if @ships[1].include?(position)
			update(position, "o", 9);
			puts(@targetHit);
			@human1.counter -= 1;
		else
			update(position, "x", 9);
			puts(@targetMissed);
		end
	end

	def second_player
		if @num == 1
			position = @cpu2.generate_position("#{@cpuShips}", @ships_list2);
		else
			position = @human2.generate_position("#{@player2atatck}", @ships_list2);
		end
		puts("Missile thrown at: #{position}");
		@ships_list2 << position;
		if @ships[0].include?(position)
			update(position, "o", 0);
			puts(@targetHit);
			@cpu2.counter -= 1 if @num == 1;
			@human2.counter -= 1 if @num == 2;
		else
			update(position, "x", 0);
			puts(@targetMissed);
		end
	end
end

def main
	game = Game.new;
	game.get_players;
	game.get_ships;
	game.attack;
end

main;
