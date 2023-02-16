def line_rec(n):
	if(n == 1):
		return [1];
	else:
		p_line = line_rec(n - 1);
		line = [p_line[i] + p_line[i + 1] for i in range(len(p_line) - 1)];
		line.insert(0, 1);
		line.append(1);
	return line;

def line(n):
	p_line = [1];
	while n > 1:
		line = [1];
		for i in range(len(p_line) - 1):
			line.append(p_line[i] + p_line[i + 1]);
		line.append(1);
		p_line = line;
		n -= 1;
	return p_line;

def fibonacci(n):
	tri = [];
	for i in range(1, n + 1):
		tri.append(line_rec(i));
	sum = 0;
	for i in range((n - 1), (n // 2) - 1, -1):
		sum += tri[i][(n - 1) - i];
	return sum;

def main():
	n = int(input("Input the line number: "));
	print(line_rec(n));
	print(line(n));

	for i in range(1, n + 1):
		print(fibonacci(i));

if(__name__ == "__main__"):
	main();
