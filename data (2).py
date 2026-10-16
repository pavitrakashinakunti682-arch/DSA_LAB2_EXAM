Question 4 — Apostrophe (') ಮತ್ತು Question mark (?) separators
Step 1: ಎಲ್ಲಿ paste ಮಾಡಬೇಕು?

# QUESTION 4: WORD SEPARATORS

def get_words(line):
    for sep in ".,:;?'":
        line = line.replace(sep, " ")
    return line.lower().split()
Step 2: ಈಗಿರುವ code‌ನಲ್ಲಿ ಬದಲಾವಣೆ ಮಾಡು
ನಿನ್ನ main() ಒಳಗೆ ಈ code ಹುಡುಕು:
words_by_line = [    re.findall(r"\b\w+\b", line.lower())    for line in lines]



ಅದನ್ನು ತೆಗೆದು ಈ code ಹಾಕು:
words_by_line = [
    get_words(line)
    for line in lines
]Step 3: ಇದು ಏನು ಮಾಡುತ್ತದೆ?
- ? ಇದ್ದರೆ ಅದನ್ನು space ಆಗಿ ಬದಲಿಸುತ್ತದೆ.
- ' ಇದ್ದರೆ ಅದನ್ನು space ಆಗಿ ಬದಲಿಸುತ್ತದೆ.
- ಇತರ ಕೊಟ್ಟಿರುವ punctuation‌ಗಳನ್ನೂ space ಆಗಿ ಬದಲಿಸುತ್ತದೆ.
- ನಂತರ ಪದಗಳನ್ನು lowercase‌ನಲ್ಲಿ ಬೇರ್ಪಡಿಸುತ್ತದೆ.
ಉದಾಹರಣೆ:
What's your name?
ಪದಗಳಾಗಿ ಹೀಗೆ ಸಿಗುತ್ತದೆ:
what
s
your
name

Question 5 — Ignore empty tokens and keep printable punctuation
Step 1: ಏನು ಮಾಡಬೇಕು?
ನಿನ್ನ ಈಗಿನ code‌ನಲ್ಲಿ ಹೊಸ code paste ಮಾಡುವ ಅವಶ್ಯಕತೆ ಇಲ್ಲ. ನೀನು Question 4ರಲ್ಲಿ ಹಾಕಿದ 
get_words() function ಸಾಕು.

def get_words(line):
    for sep in ".,:;?'":
        line = line.replace(sep, " ")
    return line.lower().split()


Question 6 — Store duplicate line numbers
Step 1: ಯಾವ code ಹುಡುಕಬೇಕು?
ನಿನ್ನ Python file‌ನಲ್ಲಿ LineQueue class ಒಳಗೆ ಈ function ಹುಡುಕು:


def add(self, line):
    node = Node(line)

    if self.head is None:
        self.head = node
    else:
        self.tail.next = node

    self.tail = node


Step 3: Output ಹೇಗೆ ಬದಲಾಗುತ್ತದೆ?
Input:
cat cat cat
ಹಳೆಯ ವಿಧಾನ:
cat: 1
question 6 ಬದಲಾವಣೆಯ ನಂತರ:
cat: 1, 1, 1

Bhai ❤️ ಈಗ Question 7 — Add a count() method to LineQueue ಮಾಡೋಣ!
ನಿನ್ನ PDF ಪ್ರಕಾರ, LineQueueನಲ್ಲಿ ಎಷ್ಟು line-number nodes ಇವೆ ಎಂದು ಎಣಿಸುವ method ಸೇರಿಸಬೇಕು. index_generation_lab_exam_modification_guide-1.pdf

Step 1: ಎಲ್ಲಿ paste ಮಾಡಬೇಕು?
ನಿನ್ನ Python file‌ನಲ್ಲಿ class LineQueue: ಹುಡುಕು.
ಅದರೊಳಗೆ ಇರುವ add() method ಮುಗಿದ ನಂತರ, ಆದರೆ LineQueue class‌ನ indentation ಒಳಗೆ ಈ code paste ಮಾಡು.


def count(self):
    total = 0
    cur = self.head

    while cur is not None:
        total += 1
        cur = cur.next

    return total
Step 2: ಇದು ಏನು ಮಾಡುತ್ತದೆ?
ಉದಾಹರಣೆಗೆ, queueನಲ್ಲಿ line numbers ಹೀಗಿದ್ದರೆ:
2 → 4 → 6


Output:
3

Question: Modify LineQueue to add a method named contains_line(line) that returns True if the given line number already exists in the queue; otherwise, return False. index_generation_lab_exam_modification_guide-1.pdf

Step 1: ಎಲ್ಲಿ paste ಮಾಡಬೇಕು?
ನಿನ್ನ Python file‌ನಲ್ಲಿ class LineQueue: ಹುಡುಕು. ಅದರೊಳಗೆ def count(self): method ಇದ್ದರೆ, ಅದರ ನಂತರ ಈ code paste ಮಾಡು.

def contains_line(self, line):
    cur = self.head

    while cur is not None:
        if cur.line == line:
            return True
        cur = cur.next

    return False


Question 9 — Print only words with at least N indexed lines
Question: Modify the dictionary output function to print only those words that appear on at least N different lines. index_generation_lab_exam_modification_guide-1.pdf


input index
apple: [1, 2, 4]
banana: [3]
mango: [2, 5]
orange: [6]

Expected output:
apple: [1, 2, 4]
mango: [2, 5]


apple ಮತ್ತು mango ಮಾತ್ರ ಎರಡು ಅಥವಾ ಹೆಚ್ಚು lines‌ನಲ್ಲಿ ಬಂದಿವೆ.
Step 2: ಯಾವ code ಬದಲಾಯಿಸಬೇಕು?
ನಿನ್ನ PDFನ ಮೂಲ project‌ನಲ್ಲಿ write() function ಇದೆ. Dictionary version‌ಗೆ ಉದಾಹರಣೆ:

def write(index, outname, min_lines=1):
    with open(outname, "w", encoding="utf-8") as out:
        for word in sorted(index):
            if index[word].count() >= min_lines:
                out.write(
                    word + ": " + index[word].text() + "\n"
                )

Step 3: ನಿನ್ನ ಈಗಿನ code‌ಗೆ ಸರಿಯಾದ ಬದಲಾವಣೆ
ನಿನ್ನ DictionaryIndex class‌ನ print_index() method ಅನ್ನು ಹೀಗೆ ಬದಲಾಯಿಸಬಹುದು:


def print_index(self, min_lines=1):
    return [
        f"{word}: {self.index[word]}"
        for word in sorted(self.index)
        if len(set(self.index[word])) >= min_lines
    ]
ನಂತರ main()ನಲ್ಲಿ ಈಗಿರುವ:
output = index.print_index()
ಇದನ್ನು ಹೀಗೆ ಬದಲಾಯಿಸು:
output = index.print_index(min_lines=2)

Question 10
Question: Add a prefix search function to the Trie that returns all complete words starting with a given prefix.
ಕನ್ನಡದಲ್ಲಿ: ಕೊಟ್ಟಿರುವ ಆರಂಭದ ಅಕ್ಷರಗಳಿಂದ ಶುರುವಾಗುವ ಎಲ್ಲಾ ಪದಗಳನ್ನು ಹುಡುಕಬೇಕು.
ಉದಾಹರಣೆ: Prefix app ಕೊಟ್ಟರೆ app, apple, application ಹೀಗೆ ಆ prefix‌ನಿಂದ ಶುರುವಾಗುವ ಪದಗಳು ಸಿಗಬೇಕು (inputನಲ್ಲಿ ಇದ್ದರೆ ಮಾತ್ರ).
Step 1: ಎಲ್ಲಿ paste ಮಾಡಬೇಕು?
ನಿನ್ನ code‌ನಲ್ಲಿರುವ class Trie: ಹುಡುಕು. ಅದರೊಳಗೆ ಇರುವ search() method ನಂತರ, print_index() method ಮೊದಲು ಈ function paste ಮಾಡು.


def prefix_search(self, prefix):
    node = self.root

    for char in prefix:
        if char not in node.children:
            return []
        node = node.children[char]

    found = []

    def collect(cur, word):
        if cur.lines:
            found.append(word)

        for char in sorted(cur.children):
            collect(cur.children[char], word + char)

    collect(node, prefix)
    return found

Step 2: ಹೇಗೆ test ಮಾಡುವುದು?
ನಿನ್ನ main()ನಲ್ಲಿ Trie object build ಮಾಡಿದ ನಂತರ ಈ line test ಮಾಡಬಹುದು:
print("Prefix search:", index.prefix_search("app"))

Question 11
Question: Modify the word index to store the total frequency (number of occurrences) of each word,
 along with the line numbers where it appears.
ಕನ್ನಡದಲ್ಲಿ: ಒಂದು ಪದ ಎಷ್ಟು ಬಾರಿ ಬಂದಿದೆ ಎಂದು ಎಣಿಸಬೇಕು. ಆ ಪದ ಯಾವ linesನಲ್ಲಿ ಬಂದಿದೆ ಎಂಬ ಮಾಹಿತಿಯನ್ನೂ ಉಳಿಸಬೇಕು.
Step 1: Example ಅರ್ಥಮಾಡಿಕೋ
Input:
apple apple mango
apple mango


Expected output:
apple: 1, 2 (count=3)
mango: 1, 2 (count=2)


- apple ಒಟ್ಟು 3 ಬಾರಿ ಬಂದಿದೆ.
- mango ಒಟ್ಟು 2 ಬಾರಿ ಬಂದಿದೆ.
- Line numbers ಮಾತ್ರವಲ್ಲದೆ, ಪದದ ಒಟ್ಟು occurrences ಕೂಡ ಬೇಕು.
Step 2: ಯಾವ code ಬದಲಾಯಿಸಬೇಕು?
ನಿನ್ನ PDF ಪ್ರಕಾರ, Dictionary versionನಲ್ಲಿ build(), search() ಮತ್ತು write() ಬದಲಾಯಿಸಬೇಕು. index_generation_lab_exam_modification_guide-1.pdf

ನಿನ್ನ ಈಗಿನ codeನ DictionaryIndex classನಲ್ಲಿ build() method ಅನ್ನು ಈ ರೀತಿ ಬದಲಾಯಿಸು:

class DictionaryIndex:
    def __init__(self):
        self.index = {}

    def build(self, words_by_line):
        for line_no, words in enumerate(words_by_line, 1):
            for word in words:
                if word not in self.index:
                    self.index[word] = {
                        "lines": [],
                        "frequency": 0
                    }

                self.index[word]["frequency"] += 1

                if line_no not in self.index[word]["lines"]:
                    self.index[word]["lines"].append(line_no)


Bhai ❤️ ಈಗ Question 12 — Count BST Words ಮಾಡೋಣ!
index_generation_lab_exam_modification_guide-1.pdf
Question 12
Question: Add a function that returns the number of distinct words stored in a Binary Search Tree (BST).
ಕನ್ನಡದಲ್ಲಿ: BSTಯಲ್ಲಿ ಎಷ್ಟು ವಿಭಿನ್ನ ಪದಗಳಿವೆ ಎಂದು ಎಣಿಸುವ function ಬರೆಯಬೇಕು. ಒಂದೇ ಪದ ಹಲವು ಬಾರಿ ಬಂದರೂ ಅದನ್ನು ಒಂದೇ ಪದವಾಗಿ ಎಣಿಸಬೇಕು.
Step 1: ಎಲ್ಲಿ paste ಮಾಡಬೇಕು?
ನಿನ್ನ Python file‌ನಲ್ಲಿ class BST: ಮುಗಿದ ನಂತರ, class TrieNode: ಶುರುವಾಗುವ ಮೊದಲು ಈ function paste ಮಾಡು.


def count_words(node):
    if node is None:
        return 0

    return (
        1
        + count_words(node.left)
        + count_words(node.right)
    )
Step 2: ಹೇಗೆ test ಮಾಡುವುದು?
ನಿನ್ನ main()ನಲ್ಲಿ BST build ಆದ ನಂತರ:
print("Distinct words:", count_words(index.root))
ಗಮನಿಸಿ: ಈ test ಅನ್ನು index ಒಂದು BST object ಆಗಿರುವಾಗ ಮಾತ್ರ ಬಳಸಬೇಕು.
Step 3: Example
BSTನಲ್ಲಿ apple, banana, mango ಎಂಬ ಮೂರು ವಿಭಿನ್ನ ಪದಗಳಿದ್ದರೆ:
Distinct words: 3



Question 13
Question: Rewrite the BST output function iteratively instead of recursively, while preserving lexicographic (alphabetical) order.

Step 1: ಯಾವ code paste ಮಾಡಬೇಕು?
ನಿನ್ನ class BST: ಒಳಗೆ ಇರುವ print_index() method ಅನ್ನು ಕೆಳಗಿನ codeನಿಂದ replace ಮಾಡು.


def print_index(self):
    result = []
    stack = []
    node = self.root

    while stack or node:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        result.append(f"{node.word}: {node.lines}")
        node = node.right

    return result
BSTಯಲ್ಲಿ mango, apple, banana, orange ಇದ್ದರೆ:
apple: [2]
banana: [3]
mango: [1]
orange: [4]

Bhai ❤️ ಈಗ Question 14 — Add a Trie Word Count ಮಾಡೋಣ!
index_generation_lab_exam_modification_guide-1.pdf
Question a
Question: Add a function to count the number of complete words stored in a Trie, not the total number of character nodes.
ಕನ್ನಡದಲ್ಲಿ: Trieನಲ್ಲಿ ಎಷ್ಟು ಸಂಪೂರ್ಣ ಪದಗಳಿವೆ ಎಂದು ಎಣಿಸಬೇಕು. ಕೇವಲ ಅಕ್ಷರಗಳ nodesಗಳನ್ನು ಎಣಿಸಬಾರದು.
Step 1: ಎಲ್ಲಿ paste ಮಾಡಬೇಕು?
ನಿನ್ನ Python fileನಲ್ಲಿ class Trie: ಮುಗಿದ ನಂತರ, def main(): ಬರುವ ಮೊದಲು ಈ function paste ಮಾಡು.


def count_trie_words(node):
    total = 1 if node.lines else 0

    for child in node.children.values():
        total += count_trie_words(child)

    return total

Step 2: ಹೇಗೆ test ಮಾಡುವುದು?
ನಿನ್ನ main()ನಲ್ಲಿ Trie build ಆದ ನಂತರ ಈ line ಬಳಸು:
print("Trie word count:", count_trie_words(index.root))

Step 3: ಉದಾಹರಣೆ
Trieನಲ್ಲಿ app, apple, bat ಎಂಬ ಮೂರು ಸಂಪೂರ್ಣ ಪದಗಳಿದ್ದರೆ:
Trie word count: 3


- node.lines ಇದ್ದರೆ ಆ node ಒಂದು ಸಂಪೂರ್ಣ ಪದವನ್ನು ಸೂಚಿಸುತ್ತದೆ.
-
Bhai ❤️ ಈಗ Question 15 — Make Benchmark Runs Reproducible ಮಾಡೋಣ!
index_generation_lab_exam_modification_guide-1.pdf
Question 15
Question: Modify the benchmark program so that random test data is repeatable across runs.
ಕನ್ನಡದಲ್ಲಿ: ಪ್ರೋಗ್ರಾಂ ಅನ್ನು ಮತ್ತೆ ಮತ್ತೆ run ಮಾಡಿದಾಗಲೂ ಒಂದೇ random sequence ಬರಬೇಕು.
Step 1: ಎಲ್ಲಿ paste ಮಾಡಬೇಕು?
ನಿನ್ನ benchmark.py ಫೈಲ್ ತೆರೆಯು. ಮೇಲ್ಭಾಗದಲ್ಲಿ ಈ import ಇರಬೇಕು:
import random
import random

random.seed(42)

# Remaining benchmark code

Bhai ❤️ ಈಗ Question 16 — Benchmark Successful and Unsuccessful Searches ಮಾಡೋಣ!
index_generation_lab_exam_modification_guide-1.pdf
Question 16
Question: Modify the benchmark program to measure the time taken by successful searches (hits) and unsuccessful searches (misses) separately.
ಕನ್ನಡದಲ್ಲಿ: ಪದ ಸಿಕ್ಕಾಗ ಎಷ್ಟು ಸಮಯ ಬೇಕಾಗುತ್ತದೆ ಮತ್ತು ಪದ ಸಿಗದಾಗ ಎಷ್ಟು ಸಮಯ ಬೇಕಾಗುತ್ತದೆ ಎಂದು ಪ್ರತ್ಯೇಕವಾಗಿ ಅಳೆಯಬೇಕು.
Step 1: ಯಾವ code paste ಮಾಡಬೇಕು?
ನಿನ್ನ benchmark.py ಫೈಲ್‌ನಲ್ಲಿ index build ಮಾಡಿದ ನಂತರ ಈ code paste ಮಾಡು.

# Successful searches (hits)
hits = random.choices(vocab, k=50000)

t = time.time()
for word in hits:
    m.search(index, word)
hit_time = time.time() - t

# Unsuccessful searches (misses)
misses = ["NOT_PRESENT_" + str(i) for i in range(50000)]

t = time.time()
for word in misses:
    m.search(index, word)
miss_time = time.time() - t

print(name, "hit:", round(hit_time, 3),
      "miss:", round(miss_time, 3))


Question 17 — Calculate Average Search Time
Question: Modify the benchmark program to calculate the average time taken for each search.
ಕನ್ನಡದಲ್ಲಿ: ಒಂದು word search ಮಾಡಲು ತೆಗೆದುಕೊಳ್ಳುವ ಒಟ್ಟು ಸಮಯವನ್ನು, ಮಾಡಿದ searches ಸಂಖ್ಯೆಯಿಂದ divide ಮಾಡಿ, ಒಂದು search ಗೆ ಸರಾಸರಿ ಎಷ್ಟು ಸಮಯ ಬೇಕು ಎಂದು ಕಂಡುಹಿಡಿಯಬೇಕು.
Step 1: ಎಲ್ಲಿ paste ಮಾಡಬೇಕು?
ನಿನ್ನ benchmark.py ಫೈಲ್ open ಮಾಡು.
ಮೇಲ್ಭಾಗದಲ್ಲಿ ಈ imports ಇರಬೇಕು:
import time
ಈಗಾಗಲೇ import time ಇದ್ದರೆ ಮತ್ತೆ add ಮಾಡಬೇಡ.
Step 2: ಈ function paste ಮಾಡು
ನಿನ್ನ benchmark.py ಫೈಲ್‌ನಲ್ಲಿ, ಬೇರೆ functions ಇರುವ ಜಾಗದಲ್ಲಿ ಈ code paste ಮಾಡು. main function ಇದ್ದರೆ ಅದರ ಮೇಲ್ಭಾಗದಲ್ಲಿ paste ಮಾಡಬಹುದು.

def average_search_time(index, words):
    if not words:
        return 0

    start = time.perf_counter()

    for word in words:
        index.search(word)

    end = time.perf_counter()

    total_time = end - start
    average_time = total_time / len(words)

    return average_time
Step 4: Function ಅನ್ನು ಹೇಗೆ call ಮಾಡಬೇಕು?
ನಿನ್ನ index build ಆದ ನಂತರ, benchmark code ಇರುವ ಜಾಗದಲ್ಲಿ ಇದನ್ನು add ಮಾಡು:


words = ["apple", "banana", "cat"]

cಈಗಾಗಲೇ with open() ಬಳಸುತ್ತಿದ್ದರೆ, ಈ question ಬಹುಶಃ ಈಗಾಗಲೇ implemented ಆಗಿದೆ.
Step 2: Output ಬರೆಯಲು ಈ code ಬಳಸು
ನಿನ್ನ output ಬರೆಯುವ function ಒಳಗೆ ಅಥವಾ output ಬರೆಯುವ section ನಲ್ಲಿ paste ಮಾಡು.
output_path = "output.txt"with open(output_path, "w", encoding="utf-8") as file:    
file.write("Word Index\n")    
file.write("apple: 1, 2\n")   
 file.write("banana: 2, 3\n")


Program run ಆದ ಮೇಲೆ ನಿನ್ನ project folder ನಲ್ಲಿ output.txt open ಮಾಡಿ output check ಮಾಡು.
Step 5: Expected output
output.txt file ಒಳಗೆ:
Word Index
apple: 1, 2
banana: 2, 3

18 QUESTIONS
Step 3: Where to add
def write(index, outname):
    with open(outname, "w", encoding="utf-8") as out:
        # Keep your existing writing loop here
        pass

STEP2:- REPLACE
with open(outname, "w", encoding="utf-8") as out:

Q22. Count complete Trie words
File: trie_index.py
Where: Class ಹೊರಗೆ add ಮಾಡು.
def count_words(node):
    total = 1 if node.lines is not None else 0
    for child in node.children.values():
        total += count_words(child)
    return total


Q23. Safe search for missing words
File: dict_index.py, bst_index.py, ಅಥವಾ trie_index.py
Where: search() function ನಂತರ add ಮಾಡು.

def search_lines(index, word):
    q = search(index, word)
    if q is None: return []
    return q.text()

Q24. Repeatable random data
File: benchmark.py
Where: Imports ನಂತರ add ಮಾಡು.
import randomrandom.seed(42)



Q25. Sort dictionary output
File: dict_index.py
Where: write() functionನಲ್ಲಿ existing loop replace ಮಾಡು.
Replace this:
for word in index:
STEP :-2
for word in sorted(index):











