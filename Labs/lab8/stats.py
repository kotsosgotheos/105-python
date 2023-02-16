def transactions(csvfile):
	first = csvfile.readline();
	counter = 0;
	d = {};
	s = {};
	for line in csvfile.readlines():
		line = line.split(",");
		if int(line[6]) > 2000:
			counter += int(line[9]);

		if line[7] not in d:
			d[line[7]] = 1;
			s[line[7]] = int(line[6]);
		else:
			d[line[7]] += 1;
			s[line[7]] += int(line[6]);

	return counter, d, s;

def main():
	stats = open("stats.txt", "w");
	csvfile = open("Sacramentorealestatetransactions.csv", "r");
	value, trans, average = transactions(csvfile);

	stats.write("Total value of transactions of properties at least 2000 sq.f.: " + str(value) + "\n\n");

	stats.write("Total number of transactions per property type:\n\t");
	for item in trans:
		stats.write(item + ": " + str(trans[item]) + "\n\t");
	stats.write("\n");

	stats.write("Average size of sold properties per property type: \n\t");
	for item in average:
		stats.write(item + ": " + str(format(average[item] / trans[item], ".2f")) + "\n\t");
	stats.write("\n");

	stats.flush();
	stats.close();
	csvfile.close();

if(__name__ == "__main__"):
	main();
