import mark_analysis
from login import login
from mental_health_test import mental_health_test_menu


def print_main_menu():
	while True:
		print("1. Historical score data")
		print("2. mental health test")
		choice = input("Enter the number of your choice: ")
		if choice == "1":
			mark_analysis.historical_mark_data_menu()
		elif choice == "2":
			mental_health_test_menu()
		else: break

login_res = login()  # get the result of login
if login_res == 1:
	mark_analysis.get_mark()
	print_main_menu()
elif login_res == 2:
	mark_analysis.mark_init()