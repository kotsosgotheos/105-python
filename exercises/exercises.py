from functools import reduce
import random

one = lambda num: reduce(lambda a, x: a + x, list(map(int, str(num))), 0) if int(num) % 3 == 0 else int(num) // 2 if int(num) % 2 == 0 else num;
print(one(input("1. Please enter a number: ")));

two = lambda age, movies: movies["1"] if age < 15 else movies["1"] + movies["15"] if age >= 15 and age < 18 else movies["1"] + movies["15"] + movies["18"];
print(two(int(input("2. Please enter your age: ")), {"1": [1, 2, 3], "15": [4, 5, 6], "18": [7, 8, 9]}));

def three(str):
	str_to_int = lambda str: list(map(int, str.split(",")));
	list_sum = lambda str: reduce(lambda a, x: a + x, str_to_int(str));
	number_list = str_to_int(str);
	number_list.append(list_sum(str)) if list_sum(str) % 2 == 0 else number_list.insert(0, list_sum(str));
	return number_list;
print(three(input("3. Please enter a list of numbers divided by a comma: ")));

four = list(set(list(filter(lambda i: i not in [random.randint(1, 15) for x in range(10)], [random.randint(1, 15) for x in range(10)]))));
print("4. Unique numbers:\n%s" %(four));

five = lambda text: len(list(filter(lambda x: x[0] == 'a', text.split())));
print(five(input("5. Please enter some text: ")));

six = lambda str: True if str[0] == str[-1] else False;
print(six(input("6. Please enter a string: ")));

seven = lambda numbers: reduce(lambda a, x: a + x, list(filter(lambda x: x % 2 == 0, list(map(int, numbers.split(","))))));
print(seven(input("7. Please enter a list of numbers divided by a comma: ")));

eight = lambda num, c_num: "Human wins" if (num < c_num and c_num != 3) or (num < c_num and c_num == 3 and num != 1) or (c_num < num and num == 3 and c_num == 1) else "Computer wins" if (num < c_num and c_num == 3 and num == 1) or (c_num < num and num != 3) or (c_num < num and num == 3 and c_num != 1) else "Its a draw";
print(eight(int(input("8. Please enter a number from 1-3: ")), random.randint(1, 3)));

nine = lambda randnum, guess: "You found the number" if randnum == guess else nine(randnum, int(input("Your number is lower than the random one. Try again: "))) if randnum > guess else nine(randnum, int(input("Your number is greater than the random one. Try again: ")));
print(nine(random.randint(1, 100), int(input("9. Please enter a number between 1 and 100: "))));

ten = lambda lst: list(filter(lambda x: lst.count(x) >= 2, lst));
print("10.",*list(set(ten([random.randint(1, 10) for x in range(10)]))));

eleven = lambda text: " ".join(list(reversed(text.split())));
print(eleven(input("11. Please enter some text: ")));

twelve = lambda x, counter: counter if x < 10 else twelve(x * 0.9, counter + 1);
print("12. Number of times a ball bounces from a meter high: %d" %(twelve(100, 0)));

thirteen = lambda year: (year - 1980) if (year - 1980) ** 2 == year else thirteen(year + 1);
print("13. I will be %d years old in %d" %(thirteen(1980), thirteen(1980) ** 2));

fourteen = lambda original, value, counter: counter if value < original * 0.3 else fourteen(original, value * 0.85, counter + 1);
print("14. Number of years for value of car to drop to 30%% of original: %d" %(fourteen(1, 1, 0)));

fifteen = lambda word: len(set(list(filter(lambda c: c in "aeiou", [i for i in word]))));
print(fifteen(input("15. Please enter a word: ")));

sixteen = lambda text: "".join(["" if char == "r" else char for word in list(map(lambda word: word + " ", text.split())) for char in word]);
print(sixteen(input("16. Please enter some text: ")));

seventeen = lambda numbers: reduce(lambda x, a: a + x, [1 if digit == "1" else 0 for num in numbers for digit in str(num)]);
print("17.",seventeen(range(0, 999999)));

eighteen = lambda numbers: reduce(lambda x, a: a + x, [len(str(num)) for num in numbers]);
print("18.",eighteen(range(1, 1000000)));
