import json

def read_json(file_name): #open json and return
	with open(file_name, "r") as f:
		return json.load(f)

def save_json(file_name, data): #save json
	with open(file_name, "w") as f:
		json.dump(data, f, indent = 4)