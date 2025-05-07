import bisect
import general_tools
from datetime import datetime
mark_data = general_tools.read_json("mark_data.json")

def _longest_increasing_score():
	smallest_value = [0x3f3f3f] * (len(mark_data["sum"]) + 1)  # initialize with INF
	smallest_value[0] = 0
	max_value = 0
	latest_value = 0
	for i in mark_data["history"].values():
		pos = bisect.bisect_right(smallest_value, i)  # use binary search to find the first value that is greater than i
		latest_value = pos  # the longest increasing subsequence end with i is pos
		smallest_value[pos] = i  # the smallest end number is i
		if latest_value > max_value:
			max_value = latest_value
	print(f"Your score hasn't dropped for {latest_value} days!")
	print(f"So far, your record is {max_value} days!\n")

def _avg_mark(day = 7):
	if len(mark_data["sum"]) < day:
		return mark_data["sum"][-1] - mark_data["sum"][0] / len(mark_data["sum"])
	return mark_data["sum"][-1] - mark_data["sum"][-day - 1] / day  # use prefix sum to calculate the average mark

def mark_init():
	mark_data["sum"] = [0]
	mark_data["history"] = {}  # clear the data
	general_tools.save_json("mark_data.json", mark_data)

def get_mark():
	date = str(datetime.now().strftime("%Y-%m-%d"))  # get the date today
	print("Today is " + date)
	if date in mark_data["history"]:
		print("You have already scored today.\n")
		return # return if user have marked today
	mark = general_tools.get_int_in_range("Please rate your mood today (0-10):", 0, 10)
	mark_data["history"][date] =  mark  # add the mark today to the history
	mark_data["sum"].append(mark_data["sum"][-1] + mark)  # prefix sum of the mark
	if _avg_mark() >= 5:  # ive users feedback based on the average score over the past 7 days
		print("Your recent mood rating is quite high! Keep up the positive vibes!")
	else:
		print("Your recent mood rating is a bit low.")
		print("You can explore the resources in the app for ways to relax or access to mental health services.")
	_longest_increasing_score()  # give user feedback about his score change trend
	general_tools.save_json("mark_data.json", mark_data)  # save the history

def historical_mark_data_menu():
	while True:
		print("1. View your mood score for specific date")
		print("2. View your average mood score for specific period")
		print("3. Exit")
		choice = input("Please enter your choice:")
		print()
		if choice == "1":
			date = input("Please enter the date you want to view (YYYY-MM-DD):")
			if date in mark_data["history"]:
				print(f"The mood score for {date} is {mark_data['history'][date]}\n")
			else:
				print("No score recorded for " + date + '\n')  # date not in dictionary
		elif choice == "2":
			day = general_tools.get_int("Please enter the period you want to view (1-7):")
			print(f"The average mood score for the past {day} days is {_avg_mark(day)}\n")  # get average mark
		else: 
			break # exit