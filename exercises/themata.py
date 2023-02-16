lcm = lambda lst, multi: max(lst) * multi if len(list(filter(lambda item: (max(lst) * multi) % item == 0, lst))) == len(lst) else lcm(lst, multi + 1);
num = lcm([6,12,15], 1);
print(num);

