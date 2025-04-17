
import os
from datetime import datetime
import general_tools

# Define order for diary navigation
order = ["year", "month", "day"]
path_today = "user_diary/" + datetime.now().strftime("%Y/%m/%d")

class Queue:
	# Queue implementation for AC automaton
	max_size = 10005

	def __init__(self):
		self.queue = [0] * Queue.max_size
		self.tail = 0

	def push(self, val):
		self.tail += 1
		self.queue[self.tail] = val

	def pop(self):
		self.tail -= 1

	def front(self):
		return self.queue[self.tail]

	def empty(self):
		return self.tail == 0


class AcAutomata:
	# Aho-Corasick automaton for sensitive word detection
	root = 1
	sigma_size = 30
	max_node = Queue.max_size

	def __init__(self):
		self.node_cnt = 1
		self.end = [False] * AcAutomata.max_node
		self.trie = [[0] * AcAutomata.sigma_size for _ in range(AcAutomata.max_node)]
		self.fail = [0] * AcAutomata.max_node

	@staticmethod
	def _index(char):
		# Convert character to index for trie
		if char == ' ':
			return 0
		elif char == '\'':
			return 1
		elif char == '-':
			return 2
		else:
			return ord(char.lower()) - ord('a') + 3

	def _insert(self, string):
		# Insert a word into the trie
		u = AcAutomata.root
		for i in string:
			idx = self._index(i)
			if not self.trie[u][idx]:
				self.node_cnt += 1
				self.trie[u][idx] = self.node_cnt
			u = self.trie[u][idx]
		self.end[u] = True

	def _build_fail(self):
		# Build failure links for AC automaton
		q = Queue()
		for i in range(self.sigma_size):
			if self.trie[AcAutomata.root][i]:
				self.fail[self.trie[AcAutomata.root][i]] = AcAutomata.root
				q.push(self.trie[AcAutomata.root][i])
			else:
				self.trie[AcAutomata.root][i] = AcAutomata.root
		while not q.empty():
			u = q.front()
			q.pop()
			for i in range(self.sigma_size):
				if self.trie[u][i]:
					self.fail[self.trie[u][i]] = self.trie[self.fail[u]][i]
					q.push(self.trie[u][i])
				else:
					self.trie[u][i] = self.trie[self.fail[u]][i]

	def _find(self, string):
		# Find sensitive words in input string
		u = AcAutomata.root
		pos = 0
		for i in string:
			pos += 1
			if i != ' ' and not i.islower():
				u = 0
				continue
			u = self.trie[u][self._index(i)]
			if self.end[u]:
				return pos
		return 0

	def init_ac_automata(self):
		# Initialize AC automaton with sensitive words
		word_list = general_tools.read_txt_line("sensitive_words_list.txt")
		for i in word_list:
			self._insert(i.strip())
		self._build_fail()

	def find_sensitive_word(self, string):
		# Check for sensitive words and handle user response
		res = self._find(string.lower())
		if res:
			print(f"A sensitive word was found end at character {res} in your diary. If you're feeling down, "
				  f"Don't worry — we're here to support you.")
			choice = input("if you want to rewrite your entry, type \"yes\", otherwise we will keep your entry: ")
			print()
			if choice == "yes":
				return False
			else: 
				return True
		return True

def _add_diary():
	# Add or update diary entry for today
	if os.path.exists(path_today):
		print("Here is your diary entry for today: ")
		print(general_tools.read_txt(path_today + "/content.txt"))
	else:
		print("Seems like you haven't written a diary for today yet.")
		os.makedirs(path_today)
	print()
	content = input("Please enter the content you want to add to your diary: ")
	print()
	if check_sensitive_word.find_sensitive_word(content):
		general_tools.save_txt(path_today + "/content.txt", "a", content)
		print("Your diary entry has been saved successfully!")
	else:
		print("Your diary entry has not been saved.")
	print()

def _write_diary():
	# Main diary writing interface
	while True:
		print("1. Add content to your diary")
		print("2. Rewrite your diary")
		print("3. Exit")
		choice = input("Please enter the number of your choice: ")
		print()
		if choice == "1":
			_add_diary()
		elif choice == "2":
			if os.path.exists(path_today) :
				os.remove(path_today + "/content.txt")
				os.removedirs(path_today)
				print("Your diary entry has been deleted successfully!\n")
			else:
				print("You haven't written a diary for today yet.\n")
		elif choice == "3":
			print()
			break  # exit
		else:
			print("Invalid choice!\n")

def _view_diary(file_path = "user_diary/", cnt = 0):
	# Navigate and view diary entries
	if cnt == 3:
		print(general_tools.read_txt(file_path + "content.txt"))
		print()
		return
	name_list = os.listdir(file_path)
	list_len = len(name_list)
	while True:
		print(f"Please select the {order[cnt]} of the diary entry you're looking for.")
		for i in range(list_len):
			print(f"{i + 1}. {name_list[i]}")
		file = (general_tools.get_int_in_range
		("Please enter the number of the diary entry you're looking for (enter 0 to exit): ", 0, list_len))
		print()
		if file == 0: break
		_view_diary(file_path + name_list[int(file) - 1] + '/', cnt + 1)

def diary_menu():
	# Main diary menu interface
	while True:
		print("1. Write your diary")
		print("2. View your daily diary")
		print("3. Exit")
		choice = input("Please enter the number your choice: ")
		print()
		if choice == "1":
			_write_diary()
		elif choice == "2":
			if os.path.exists("user_diary/"):
				_view_diary()
			else:
				print("You don't have any diary yet.\n")
		elif choice == "3":
			break  # exit
		else:
			print("Invalid choice!")
# Initialize AC automaton for sensitive word detection
check_sensitive_word = AcAutomata()
