from datetime import datetime
import json_operate
mark_data = json_operate.read_json("mark_data.json")

def mark_init():
	mark_data["sum"] = [0]
	mark_data["history"] = {} #clear the data
	json_operate.save_json("mark_data.json", mark_data)

def avg_mark(day = 7):
	if len(mark_data["sum"]) < day:
		return mark_data["sum"][-1] - mark_data["sum"][0] / len(mark_data["sum"])
	return mark_data["sum"][-1] - mark_data["sum"][-day - 1] / day

def get_mark():
	date = datetime.now().strftime("%Y-%m-%d") #get the date today
	print("Today is " + date)
	if date in mark_data["history"]:
		print("You have already marked today.")
		return #return if user have marked today
	mark = int(input("Please enter your mood mark today (0-10): "))
	mark_data["history"][date] =  mark #add the mark today to the history
	mark_data["sum"].append(mark_data["sum"][-1] + mark) #prefix sum of the mark
	if avg_mark() >= 5: #Give users feedback based on the average score over the past 7 days
		print("Your recent mood rating is quite high! Keep up the positive vibes!")
	else:
		print("Your recent mood rating is a bit low.")
		print("You can explore the resources in the app for ways to relax or access to mental health services.")
	json_operate.save_json("mark_data.json", mark_data)  # save the history