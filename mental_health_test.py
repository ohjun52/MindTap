import txt_operate
import json_operate

def _print_test_result(choice, mark):
	cutoffs = json_operate.read_json("mental_health_test_question/severity_cutoffs.json")  # get the cutoff of each scale item
	for i in range(3):
		if mark[i] >= cutoffs[choice][str(i)][0]:
			print(f"{cutoffs[str(i)]}: Extremely severe")
		elif mark[i] >= cutoffs[choice][str(i)][1]:
			print(f"{cutoffs[str(i)]}: Severe")
		elif mark[i] >= cutoffs[choice][str(i)][2]:
			print(f"{cutoffs[str(i)]}: Moderate")
		elif mark[i] >= cutoffs[choice][str(i)][3]:
			print(f"{cutoffs[str(i)]}: Mild")
		else:
			print(f"{cutoffs[str(i)]}: Normal")  # print the state of each scale item
	print('\n')

def _run_test(choice):
	question_map = json_operate.read_json("mental_health_test_question/DASS_question_map.json")  # get the scale item of each question
	question_list = txt_operate.read_txt_line(f"mental_health_test_question/{choice}.txt")  # get question list
	print(txt_operate.read_txt(f"mental_health_test_question/{choice}_intro.txt"))
	mark = [0, 0, 0]
	for i in range(len(question_list)):
		print(question_list[i].rstrip())  #print question
		num = int(input("your choice: "))
		mark[question_map[choice][i]] += num  # add the mark of scale item
	_print_test_result(choice, mark)

def mental_health_test_menu():
	print(txt_operate.read_txt("mental_health_test_question/DASS_intro.txt"))  # print the intro of test and choosing menu
	choice = input("Please enter the number of your choice:")
	if choice == "1":
		choice = "DASS42"
	elif choice == "2":
		choice = "DASS_Y"  # the system of test
	else: return
	_run_test(choice)