import general_tools

def _print_test_result(choice, mark):
	cutoffs = general_tools.read_json("mental_health_test_question/severity_cutoffs.json")  # get the cutoff of each scale item
	for i in range(3):
		cnt = 0  # count the times of loop
		for j in cutoffs[choice][str(i)]:
			if mark[i] >= j:
				print(cutoffs["scale_items"][i] + ": " + cutoffs["severity_state"][cnt])
				break  # find the severity of this scale item
			cnt += 1
	print() # print the state of each scale item

def _run_test(choice):
	question_map = general_tools.read_json("mental_health_test_question/DASS_question_map.json")  # get the scale item of each question
	question_list = general_tools.read_txt_line(f"mental_health_test_question/{choice}.txt")  # get question list
	print(general_tools.read_txt(f"mental_health_test_question/{choice}_intro.txt"))
	mark = [0, 0, 0]
	for i in range(len(question_list)):
		print(question_list[i].rstrip())  #print question
		num = general_tools.get_int_in_range("Your choice: ", 0, 3)
		mark[question_map[choice][i]] += num  # add the mark of scale item
	print()
	_print_test_result(choice, mark)

def mental_health_test_menu():
	print(general_tools.read_txt("mental_health_test_question/DASS_intro.txt"))  # print the intro of test and choosing menu
	choice = input("Please enter the number of your choice:")
	print('')
	if choice == "1":
		choice = "DASS42"
	elif choice == "2":
		choice = "DASS_Y"  # the system of test
	else: return
	_run_test(choice)