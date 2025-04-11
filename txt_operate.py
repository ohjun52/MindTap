def read_txt(file_name):
	with open(file_name, "r") as f:
		return f.read()  # get all of txt

def read_txt_line(file_name):
	with open(file_name, "r") as f:
		return f.readlines()  # get txt in separate line

def save_txt(file_name, opr, data):
	with open(file_name, opr) as f:
		f.write(data)  # rewrite or add data to txt
