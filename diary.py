import os
from datetime import datetime
import general_tools
order = ["year", "month", "day"]

class queue:
	
	max_size = 1000005
	
	def __init__(self):
		self.queue = [0] * max_size
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

class AC_automata:

	root = 1
	max_node = 1000005
	sigma_size = 36
	
	def __init__(self):
		self.node_cnt = 1
		self.end = [False] * max_node
		self.trie = [[0] * sigma_size for _ in range(max_node)]
		self.fail = [0] * max_node

	def _index(self, char):
		if char <= '9': return ord(char) - ord('0')
		else: return ord(char) - ord('a') + 10

	def _insert(self, string)
		u = root
		for i in string:
			idx = _index(i)
			if not self.trie[u][idx]:
				node_cnt += 1
				trie[u][idx] = node_cnt
			u = trie[u][idx]
		end[u] = True

	def _build_fail(self)
		q = queue()
		for i in range(sigma_size):
			if trie[root][i]:
				fail[trie[root][i]] = root
				q.push(trie[root][i])
			else:
				trie[root][i] = root
		while not q.empty():
			u = q.front()
			q.pop()
			for i in range(sigma_size)
				if trie[u][i]:
					fail[trie[u][i]] = trie[fail[u]][i]
					q.push(trie[u][i])
				else:
					trie[u][i] = trie[fail[u]][i]
					
	def _find(self, S):
		u = root
		pos = 1
		for i in S:
			u = trie[u][_index(i)]
			if end[u]:
				return pos
			pos += 1
		return 0

	def find_sensitive_word(self, S):
		res = _find(S)
		if res:
			print(f"Sorry, your diary contains sensitive words. in the {res}th character.")
			print("Please remove them and try again.")

def _add_diary():
	date = datetime.now().strftime("%Y/%m/%d")
	if os.path.exists(date):
		print("Here is your diary entry for today:")
		print(general_tools.read_txt(date + "/content.txt"))
	else:
		print("Seems like you haven't written a diary for today yet."")
		os.mkdir(date)
	print()
	content = input("Please enter the content you want to add to your diary: ")
	

def _write_diary():
	while True:
		print("1. Add content to your diary")
		print("2. Rewrite your diary")
		print("3. Exit")
		choice = input("Please enter the number of your choice: ")
		print()
		if choice == "1":
			_add_diary()
		elif choice == "2":
			general_tools.save_txt(date + "/content.txt", "w", "")
		elif choice == "3":
			break  # exit
		else:
			print("Invalid choice!")

def _view_diary(file_path = "user_diary", cnt = 0):
	if cnt == 3:
		print(general_tools.read_txt(file_path + "content.txt"))
		print()
		return
	name_list = os.listdir(file_path)
	list_len = len(name_list)
	file_path += "/"
	while True:
		print(f"Please select the {order[cnt]} of the diary entry you're looking for.")
		for i in range(list_len):
			print(f"{i + 1}. {name_list[i]}")
		file = (general_tools.get_int_in_range
		("Please enter the number of the diary entry you're looking for (enter 0 to exit):", 0, list_len))
		print()
		if file == 0: break
		_view_diary(file_path + name_list[int(file) - 1], cnt + 1)

def diary_menu():
	while True:
		print("1. Write your diary")
		print("2. View your daily diary")
		print("3. Exit")
		choice = input("Please enter the number your choice: ")
		print()
		if choice == "1":
			_view_diary()
		elif choice == "2":

		elif choice == "3":
			break  # exit
		else:
			print("Invalid choice!")