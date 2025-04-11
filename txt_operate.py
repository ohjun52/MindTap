def read_txt(file_name):
	with open(file_name, "r") as f:
		return f.read()

def read_txt_line(file_name)
	with open(file_name, "r") as f:
		return f.readlines()

def save_txt(file_name, opr, data)
	with open(file_name, opr) as f:
		f.write(data)