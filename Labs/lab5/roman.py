def convert(n_list, mapping, i):
	if(i == len(n_list)):
		return n_list;
	n_list[i] = mapping[i][int(n_list[i])];
	return convert(n_list, mapping, i + 1);

	# OR #
	# for i in range(len(n_list)):
	# 	n_list[i] = mapping[i][int(n_list[i])];
	# return n_list;

def break_to_list(n, n_list):
	if(n < 10):
		n_list.append(n);
		return n_list;

	n_list.append(n % 10);
	return break_to_list(n // 10, n_list);

def decimal_to_roman(n):
	mapping = [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
			   ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
			   ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
			   ["", "M", "MM", "MMM"]];

	n_list = break_to_list(n, []);
	n_list = convert(n_list, mapping, 0);
	n_list.reverse();
	return "".join(n_list);

def main():
	n = int(input("Input a number between 1 and 3999: "));
	roman = decimal_to_roman(n);
	print(roman);
	return;

if(__name__ == "__main__"):
	main();
