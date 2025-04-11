import mark_analysis
from login import login

def print_main_menu():
	while True:
		print("""1. Historical score data""")
		choice = input("Enter the number of your choice: ")
		if choice == "1":
			mark_analysis.historical_mark_data_menu()
		else: break

login_res = login() #get the result of login
if login_res == 1:
	mark_analysis.get_mark()
	print_main_menu()
elif login_res == 2:
	mark_analysis.mark_init()