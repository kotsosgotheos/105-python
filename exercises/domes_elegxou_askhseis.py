from functools import reduce
import random

# 1. Γράψτε	ένα	πρόγραμμα το οποίο θα ζητάει από την είσοδο	έναν
#αριθμό. Αν	ο αριθμός είναι	πολλαπλάσιο	του	3, το πρόγραμμα
#θα	πρέπει να τυπώνει το άθροισματων ψηφίων	του. Αλλιώς	αν ο αριθμός είναι
#πολλαπλάσιο του 2,	θα πρέπει να τυπώνει το αποτέλεσμα της ακέραιας
#διαίρεσης του αριθμού με το 2. Αλλιώς,	θα πρέπει να τυπώνει τον ίδιο τον αριθμό.
#Υποδείξεις:Χρησιμοποιήστε	τις	εντολές	if,	elif,else
def one(num):
    if num % 3 == 0:
        digit_sum = 0;
        for digit in str(num):
            sum += int(digit);
            return digit_sum;
    elif num % 2 == 0:
        return num // 2;
    else:
        return num;
print(one(int(input("1. Please enter a number: "))));

#2.	Σε έναν κινηματογράφο προβάλλονται ταινίες για ενήλικες (ηλικία τουλάχιστο 18),
#ταινίες για άτομα ηλικίας τουλάχιστο 15 και ταινίες για όλες τις ηλικίες.
#Γράψτε ένα πρόγραμμα το οποίο θα ζητάει από την είσοδο την ηλικία του χρήστη.
#Το πρόγραμμα θα πρέπει να τυπώνει όλες τις κατηγορίες ταινιών που μπορεί να δει ο χρήστης.
#Π.χ. αν ο χρήστης είναι 16 θα πρέπει να τυπώνεται: movies for ages > 15 movies for adults
#Υποδείξεις: Χρησιμοποιήστε εντολές if. Σκεφτείτε αν σας χρειάζεται το else
def two(age):
    if age < 15:
        return "movies for all ages";
    elif age >= 15 and age < 18:
        return "movies for ages > 15";
    else:
        return "movies for adults";
print(two(int(input("2. Please enter your age: "))));

#3.	Γράψτε ένα πρόγραμμα το οποίο θα ζητάει από το χρήστη μια σειρά από αριθμούς
#χωρισμένους με κόμματα και θα τους βάζει σε μια λίστα. Μετά το πρόγραμμα
#θα υπολογίζει το άθροισμα των στοιχείων της λίστας. Αν το άθροισμα είναι μονό
#τότε το πρόγραμμα θα πρέπει να το εισάγει στην αρχή της λίστας,
#αλλιώς θα το προσθέτει στο τέλος της λίστας. Τέλος το πρόγραμμα θα τυπώνει τη λίστα.
#Υποδείξεις: Χρησιμοποιήστε την συνάρτηση input για να πάρετε την είσοδο από το χρήστη.
#Κατόπιν τη μέθοδο split για να σπάσετε την είσοδο σε μια λίστα από στοιχεία. Τα στοιχεία
#αυτά πρέπει να τα μετατρέψετε σε ακεραίους (int). Για τον υπολογισμό του αθροίσματος μπορείτε
#να χρησιμοποιήσετε τη συνάρτηση sum. Τέλος μπορείτε να κάνετε χρήση των μεθόδων insert
#και append για λίστες, ή κατάτμηση (slicing) για να εισάγετε νέα στοιχεία σε αυτές.
def three(str):
    str_list = str.split(",");

    int_list = [];
    for item in str_list:
        int_list.append(int(item));

        list_sum = sum(int_list);

        if list_sum % 2 == 0:
            int_list.append(list_sum);
        else:
            int_list.insert(0, list_sum);
    return int_list;
print(three(input("3. Please enter a list of numbers divided by a comma: ")));

#4.	Γράψτε ένα πρόγραμμα το οποίο φτιάχνει δύο λίστες, η καθεμιά από τις οποίες
#έχει 10 τυχαίους αριθμούς από το 1 έως το 15. Χρησιμοποιήστε τη βιβλιοθήκη (module)
# random και τη μέθοδο randint() από κει. Το πρόγραμμα θα πρέπει να τυπώνει τις 2 λίστες.
#Μετά το πρόγραμμα, θα πρέπει να βρίσκει και να τυπώνει τους αριθμούς της πρώτης λίστας που δεν υπάρχουν
#στη δεύτερη. Χρησιμοποιήστε επανάληψη και τον τελεστή in.
#Υποδείξεις: Χρησιμοποιήστε επανάληψη για να προσπελάσετε τα στοιχεία της πρώτης λίστας.
#Για κάθε στοιχείο πρέπει να ελέγξετε αν αυτό υπάρχει στη δεύτερη λίστα (με χρήση if).
def four():
    list1 = [];
    list2 = [];
    for x in range(10):
        list1.append(random.randint(1, 15));
        list2.append(random.randint(1, 15));
    print("list1:", list1);
    print("list2:", list2);
    for item in list1:
        if item not in list2:
            print(item);
print("4. Unique numbers:\n");
four();

#5.	Γράψτε ένα πρόγραμμα το οποίο θα ζητάει από το χρήστη μια πρόταση και θα τη σπάει
#σε λέξεις τις οποίες θα αποθηκεύει σε μια λίστα. Μετά το πρόγραμμα θα πρέπει να μετρήσει
#και να τυπώσει τον αριθμό των λέξεων στην πρόταση που αρχίζουν από a.
#Για παράδειγμα, αν η πρόταση είναι “we are two happy apes” το πρόγραμμα θα πρέπει να τυπώσει 2.
#Υποδείξεις: Χρησιμοποιήστε τη μέθοδο split για να σπάσετε την είσοδο σε λέξεις.
#Μετά αρχικοποιήστε ένα μετρητή. Μετά κάντε επανάληψη στις λέξεις και αυξήστε το
#μετρητή για κάθε λέξη που αρχίζει από a. Το πρώτο γράμμα του αλφαριθμητικού s είναι το s[0].
def five(text):
    counter = 0;
    text_list = text.split();
    for word in text_list:
        if word[0] == 'a':
            counter += 1;
    return counter;
print(five(input("5. Please enter some text: ")));

#6.	Γράψτε ένα πρόγραμμα το οποίο θα ζητάει από το χρήστη ένα αλφαριθμητικό και θα τυπώνει True
#αν το αλφαριθμητικό ξεκινάει και τελειώνει με το ίδιο γράμμα. Αλλιώς θα τυπώνει False.
#Υποδείξεις: Συγκρίνετε το χαρακτήρα στην πρώτη θέση του αλφαριθμητικού με τον χαρακτήρα στην τελευταία θέση.
def six(str):
    if str[0] == str[-1]:
        return True;
    else:
        return False;
print(six(input("6. Please enter a string: ")));

#7.	Γράψτε ένα πρόγραμμα το οποίο θα ζητάει από το χρήστη μια σειρά από αριθμούς χωρισμένους με κόμματα και θα τους
#βάζει σε μια λίστα. Μετά το πρόγραμμα θα υπολογίζει το άθροισμα των ζυγών στοιχείων της λίστας.
#Για παράδειγμα για τη λίστα [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] το αποτέλεσμα είναι 220.
#Υποδείξεις: Ακολουθήστε την υπόδειξη της άσκησης 3 για να διαβάσετε και να επεξεργαστείτε σε μια
#την είσοδο του χρήστη. Μετά κάντε επανάληψη στη λίστα και χρησιμοποιήστε if για να ελέγξετε
#το αν κάθε αριθμός που διαβάζετε από αυτή είναι μονός ή ζυγός.

def seven(numbers):
    num_list = numbers.split(",");
    sum = 0;
    for num in num_list:
        num = int(num);
        if num % 2 == 0:
            sum += num;
    return sum;
print(seven(input("7. Please enter a list of numbers divided by a comma: ")));

#8.	Γράψτε ένα πρόγραμμα το οποίο θα ζητάει από το χρήστη ένα αριθμό από το 1 εώς το 3.
#Το 1 σημαίνει «πέτρα», το 2 «ψαλίδι», και το 3 «χαρτί». Το πρόγραμμα τότε
#θα υπολογίζει ένα τυχαίο αριθμό από το 1 εώς το 3 και θα τον συγκρίνει με αυτόν του χρήστη.
#Η πέτρα κερδίζει το ψαλίδι, το ψαλίδι κερδίζει το χαρτί και το χαρτί κερδίζει την πέτρα.
#Το πρόγραμμα θα τυπώνει ποιος είναι ο νικητής ή αν το παιχνίδι βγήκε ισοπαλία.
#Μετά θα ρωτάει αν θέλουμε να ξαναπαίξουμε, και αν ναι, τότε θα επαναλαμβάνει το παιχνίδι.
#Υποδείξεις: Ακολουθήστε την υπόδειξη της άσκησης 4 για να δημιουργήσετε τυχαίους αριθμούς.
#Χρησιμοποιήστε while για να συνεχίσετε ή να σταματήσετε μετά από κάθε παιχνίδι.
def eight(num, c_num):
    if (num < c_num and c_num != 3) or (num < c_num and c_num == 3 and num != 1) or (c_num < num and num == 3 and c_num == 1):
        return "Human wins";
    elif (num < c_num and c_num == 3 and num == 1) or (c_num < num and num != 3) or (c_num < num and num == 3 and c_num != 1):
        return "Computer wins";
    else:
        return "It's a draw";
print(eight(int(input("8. Please enter a number from 1-3: ")), random.randint(1, 3)));

#9.	Γράψτε ένα πρόγραμμα το οποίο θα υπολογίζει έναν τυχαίο αριθμό από το 1 εώς το 100.
#Μετά ο χρήστης θα πρέπει να μαντέψει τον αριθμό. Για κάθε αριθμό που δίνει ο χρήστης
#το πρόγραμμα θα πρέπει να τυπώνει αν ο αριθμός είναι ίσος, μικρότερος ή μεγαλύτερος
#από τον κρυφό αριθμό. Αν είναι ίσος τότε το παιχνίδι τελειώνει αλλιώς το πρόγραμμα
#καλεί τον χρήστη να ξαναμαντέψει.
#Υποδείξεις: Χρησιμοποιήστε while για να συνεχίσετε μέχρι ο χρήστης να βρει τον κρυφό αριθμό.
def nine(randnum, guess):
    if randnum == guess:
        return "You found the number";
    elif randnum > guess:
        return nine(randnum, int(input("Your number is lower than the random one. Try again: ")));
    else:
        return nine(randnum, int(input("Your number is greater than the random one. Try again: ")));
print(nine(random.randint(1, 100), int(input("9. Please enter a number between 1 and 100: "))));

# 10. Γράψτε ένα πρόγραμμα το οποίο φτιάχνει μια λίστα με 10 τυχαίους αριθμούς
#από το 1 έως το 10. Το πρόγραμμα θα τυπώνει τη λίστα και μετά θα τυπώνει τα στοιχεία
#της λίστας τα οποία εμφανίζονται σε αυτήν τουλάχιστον 2 φορές.
#Υποδείξεις: Χρησιμοποιήστε επανάληψη και λεξικό για να μετρήσετε
#πόσες φορές τα στοιχεία της λίστας εμφανίζονται σε αυτή.
def ten(lst):
    return list(filter(lambda x: lst.count(x) >= 2, lst));
print("10.",*list(set(ten([random.randint(1, 10) for x in range(10)]))));

#11. Γράψτε ένα πρόγραμμα το οποίο θα ζητάει από το χρήστη μια πρόταση και μετά
#θα τυπώνει την πρόταση με τις λέξεις σε αντίστροφη σειρά.
#Π.χ. για είσοδο ‘My name is Michele’ η έξοδος θα είναι ‘Michele is name My’.
#Υποδείξεις: Χρησιμοποιήστε split για να σπάσετε την είσοδο σε μια λίστα από λέξεις.
#Μετά κάντε χρήση της μεθόδου αντιστροφής λίστας.
def eleven(text):
    return " ".join(list(reversed(text.split())));
print(eleven(input("11. Please enter some text: ")));

#12. Μία μπάλα αν πέσει από ύψος χ αναπηδά από το έδαφος σε ύψος 0.9*χ.
#Γράψτε ένα πρόγραμμα το οποίο υπολογίζει και τυπώνει πόσες φορές πρέπει να αναπηδήσει
#η μπάλα αν την αφήσουμε από 1 μέτρο ύψος ώστε στην τελευταία αναπήδηση
#να φτάσει σε ύψος το πολύ 10 εκατοστών.
#Υποδείξεις: Χρησιμοποιήστε while για να ελέγχετε το ύψος που φτάνει η
#μπάλα χρησιμοποιώντας το ύψος από την προηγούμενη αναπήδησηκαι αυξάνετε
#ένα μετρητή σε κάθε αναπήδηση μέχρι την πρώτη φορά που το ύψος είναι το πολύ 10 εκ.
def twelve(x, counter):
    if x < 10:
        return counter;
    else:
        return twelve(x * 0.9, counter + 1);
print("12. Number of times a ball bounces from a meter high: %d" %(twelve(100, 0)));

#13. Ένα άτομο που γεννήθηκε το	1980 ισχυρίζεται «θα είμαι χ ετών το έτος
#χ στο τετράγωνο». Γράψτε ένα πρόγραμμα	που	θα	υπολογίζει το χ.
#Υποδείξεις: Χρησιμοποιήστε	while για να αυξάνετε το έτος αρχίζονταςαπό	το έτος 1981,
#ελέγχοντας	τον	ισχυρισμό μέχρι	να φτάσετε στο σωστό χ (χ=45 το έτος χ2=2025).
def thirteen(year):
    if (year - 1980) ** 2 == year:
        return (year - 1980);
    else:
        return thirteen(year + 1);
year = thirteen(1980);
print("13. I will be %d years old in %d" %(year, year ** 2));

#14. Υποθέστε ότι ένα αυτοκίνητο χάνει το 15% της αξίας του κάθε χρόνο.
#Γράψτε ένα πρόγραμμα για να βρείτε πόσα χρόνια απαιτούνται για να φτάσει
#το αυτοκίνητο στο 30% το πολύ της αρχικής του αξίας.
#Υποδείξεις: Χρησιμοποιήστε την ίδια τεχνική με την άσκηση 12.
def fourteen(original, value, counter):
    if value < original * 0.3:
        return counter;
    else:
        return fourteen(original, value * 0.85, counter + 1);
print("14. Number of years for value of car to drop to 30%% of original: %d" %(fourteen(1, 1, 0)));

#15. Γράψτε	ένα	πρόγραμμα που θα ζητά μια λέξη από την είσοδο και θα
#μετράει τον αριθμό των διαφορετικών (δηλαδή των διακριτών) φωνηέντων στη λέξη.
#Π.χ. η λέξη successful έχει 2 διαφορετικά φωνήεντα (το u και το e).
#Υποδείξεις: Κάντε μια επανάληψη στους χαρακτήρες της λέξης.
#Μπορείτε να βάζετε τα φωνήεντα σε μια λίστα αν δεν υπάρχουν
#ήδη σε αυτή και στο τέλος να μετρήσετε το μήκος της λίστας
def fifteen(word):
    vowels = [];
    for c in word:
        if c in "aeiou":
            vowels.append(c);
    return len(set(vowels));
print(fifteen(input("15. Please enter a word: ")));

#16. Γράψτε	ένα	πρόγραμμα το οποίο να δέχεται από την είσοδο ένα κείμενο και να τυπώνει το ίδιο
#κείμενο με τη διαφορά ότι  από κάθε λέξη αφαιρούνται οι χαρακτήρες ‘r’ αν υπάρχουν.
#Για παράδειγμα αν το κείμενο εισόδου είναι "Park the car in Harvard Yard.", τότε
#η έξοδος θα πρέπει να είναι "Pak the ca in Havad Yad."
#Υποδείξεις: Σπάστε το κείμενο σε μια λίστα από λέξεις (με τη split). Μετά, με χρήση for,
#για κάθε λέξη δημιουργήστε μια νέα λέξη που έχει τα ίδια γράμματα
#εκτός από τα r. Βάλτε τις νέες λέξεις σε μια λίστα και ενώστε τις με χρήση της μεθόδου join.
sixteen = lambda text: "".join(["" if char == "r" else char for word in list(map(lambda word: word + " ", text.split())) for char in word]);
print(sixteen(input("16. Please enter some text: ")));

#17. Το	καντράν	ενός αυτοκινήτου μετράει τον αριθμό των χιλιομέτρων που έχει διανύσει.
#Εμφανίζει πάντα έναν αριθμό από το 0 έως το 999999. Γράψτε ένα πρόγραμμα
#που βρίσκει και τυπώνει πόσες φορές συνολικά εμφανίζεται το 1 σε όλους αυτούς
#τους αριθμούς. Π.χ. το 1 εμφανίζεται μία φορά στο 1,
#δύο φορές στο 101, καμία φορά στο 255, κλπ.
#Υποδείξεις: Κάντε μια επανάληψη για να πάρετε τους αριθμούς 1-999999
#με τη σειρά και για καθένα από αυτούς μετρήστε πόσες φορές εμφανίζεται το 1
#εκεί και προσθέστε τον αριθμό εμφανίσεων σε ένα	μετρητή.
seventeen = lambda numbers: reduce(lambda x, a: a + x, [1 if digit == "1" else 0 for num in numbers for digit in str(num)]);
print("17.",seventeen(range(0, 999999)));

#18. Γράψτε	ένα	πρόγραμμα το οποίο υπολογίζει και τυπώνει τον συνολικό αριθμό των ψηφίων
#όλων των ακεραίων αριθμών από το 1 εώς το 1000000.
#Υποδείξεις: Κάντε μια επανάληψη για να πάρετε τους αριθμούς 1-1000000
#με τη σειρά και για καθένα από αυτούς μετρήστε πόσα ψηφία έχει
#(είτε με διαιρέσεις με το 10 είτε με μετατροπή του σε αλφαριθμητικό).
eighteen = lambda numbers: reduce(lambda x, a: a + x, [len(str(num)) for num in numbers]);
print("18.",eighteen(range(1, 1000000)));
