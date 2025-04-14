import os
import general_tools
order = ["year", "month", "day"]

def _write_diary():


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