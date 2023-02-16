from functools import reduce
from string import ascii_letters

def min(lst):
	if len(lst) == 1:
		return lst[0];
	if lst[0] < lst[1]:
		lst[0], lst[1] = lst[1], lst[0];
	return min(lst[1:]);
print("min:", min([2,3,5,7]));

def argmin(lst):
	min_item = lst[0];
	min_i = 0;
	for i in range(len(lst)):
		if lst[i] < min_item:
			min_item = lst[i];
			min_i = i;
	return min_i;
print("argmin:", argmin([43,23,12,56,29]));

substring_count = lambda s, t: len(list(filter(lambda x: x == t, [s[i:i+len(t)] for i in range(len(s))])));
print("substring_count:", substring_count("banananenananan", "nan"));

def ascii_check(s):
	for letter in s:
		if letter not in ascii_letters:
			return False;
	return True;
print("ascii_check:", ascii_check("HelloWorld"));

def interest(value, rate, years):
	for i in range(years):
		value = value + (rate / 100 * value);
		if int(value) == value:
			value = int(value);
	return value;
print("interest:", interest(100, 20, 10));

remove_vowels = lambda s: "".join(list(filter(lambda c: c not in "AEIOUaeiou", list(s))));
print("remove_vowels:", remove_vowels("Athens"));

def medians(numbers):
	def max():
		maxvalue = numbers[0];
		for value in numbers:
			if value > maxvalue:
				maxvalue = value;
		return maxvalue;
	def min():
		minvalue = numbers[0];
		for value in numbers:
			if value < minvalue:
				minvalue = value;
		return minvalue;
	def median():
		if len(numbers) % 2 == 1:
			return sorted(numbers)[len(numbers) // 2];
		else:
			return sum(sorted(numbers)[len(numbers) // 2 - 1:len(numbers) // 2 + 1]) / 2.0;
	return (max(), min(), median());
print("medians:", medians([5, 2, 3, 8, 9, -2]));