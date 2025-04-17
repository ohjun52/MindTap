import mark_analysis
import diary
from login import login
from AI_chat import ai_chat_menu
from mental_health_test import mental_health_test_menu


def print_main_menu():
	while True:
		print("1. Historical mood score data")
		print("2. Mental health test")
		print("3. Diary")
		print("4. Chat with MindTap")
		print("5. Exit")
		choice = input("Enter the number of your choice: ")
		print()
		if choice == "1":
			mark_analysis.historical_mark_data_menu()
		elif choice == "2":
			mental_health_test_menu()
		elif choice == "3":
			diary.diary_menu()
		elif choice == "4":
			ai_chat_menu()
		elif choice == "5":
			break
		else:
			print("Invalid choice!\n")

login_res = login()  # get the result of login
if login_res == 1:
	diary.check_sensitive_word.init_ac_automata()
	mark_analysis.get_mark()
	print_main_menu()
elif login_res == 2:
	mark_analysis.mark_init()