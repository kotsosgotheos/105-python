def convert(r_list, mapping):
	decimal = 0;
	for i in range(len(r_list)):
		decimal += int(mapping[r_list[i]]);
	return decimal;

def break_to_list(r, r_list):
	ones = [];
	tens = [];
	hunds = [];
	thous = [];
	r.append("");
	i = 0;
	while i < len(r):
		if(r[i] == "M"):
			thous.append(r[i]);
		if(r[i] == "C" or r[i] == "D"):
			if(r[i] == "C" and r[i + 1] == "M"):
				hunds.append(r[i]);
				hunds.append(r[i + 1]);
				i += 1;
			else:
				hunds.append(r[i]);
		if(r[i] == "X" or r[i] == "L"):
			if(r[i] == "X" and r[i + 1] == "C"):
				tens.append(r[i]);
				tens.append(r[i + 1]);
				i += 1;
			else:
				tens.append(r[i]);
		if(r[i] == "I" or r[i] == "V"):
			if(r[i] == "I" and r[i + 1] == "X"):
				ones.append(r[i]);
				ones.append(r[i + 1]);
				i += 1;
			else:
				ones.append(r[i]);
		i += 1;

		# print(ones, tens, hunds, thous); # DEBUG
	r_list.append("".join(thous));
	r_list.append("".join(hunds));
	r_list.append("".join(tens));
	r_list.append("".join(ones));
	return r_list;

def roman_to_decimal(r):
	mapping = {"": "0", "I": "1", "II": "2", "III": "3", "IV": "4", "V": "5", "VI": "6", "VII": "7", "VIII": "8", "IX": "9",
					   "X": "10", "XX": "20", "XXX": "30", "XL": "40", "L": "50", "LX": "60", "LXX": "70", "LXXX": "80", "XC": "90",
					   "C": "100", "CC": "200", "CCC": "300", "CD": "400", "D": "500", "DC": "600", "DCC": "700", "DCCC": "800", "CM": "900",
					   "M": "1000", "MM": "2000", "MMM": "3000"};

	r_list = break_to_list(r, []);
	decimal = convert(r_list, mapping);
	return decimal;

def main():
	r = input("Input a roman number between I and MMMCMXCIX: ");
	decimal = roman_to_decimal(list(r));
	print(decimal);
	return;

if(__name__ == "__main__"):
	main();
