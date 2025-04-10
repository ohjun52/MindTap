import random
import json_operate
_mod1 = 100000007
_mod2 = 100000921 #two big prime for string hash mod
user_data = json_operate.read_json("user_data.json")  # get the data from user_data.json

def _string_hash(password, mod):
	res = 0
	base = 131
	for i in password:
		res = (res * base + ord(i)) % mod
	return res #use string hash to convert password to integer

def _create_key():
	return (f"{chr(random.randint(33, 126))}{chr(random.randint(33, 126))}"
			f"{chr(random.randint(33, 126))}{chr(random.randint(33, 126))}"
			f"{chr(random.randint(33, 126))}{chr(random.randint(33, 126))}"
			f"{chr(random.randint(33, 126))}{chr(random.randint(33, 126))}"
			f"{chr(random.randint(33, 126))}{chr(random.randint(33, 126))}"
			f"{chr(random.randint(33, 126))}{chr(random.randint(33, 126))}"
			f"{chr(random.randint(33, 126))}{chr(random.randint(33, 126))}"
			f"{chr(random.randint(33, 126))}{chr(random.randint(33, 126))}") #create a random key

def _register_account():
	user_data["name"] = input("Please enter your username: ")
	password = input("Please enter your password: ") #input user's name and password
	user_data["password_hash1"] = _string_hash(password, _mod1)
	user_data["password_hash2"] = _string_hash(password, _mod2)  #use 2 mod to prevent hash collision
	print("Your account has been created successfully, Welcome to MindTap!")
	print("Please remember your key, as it will be used to recover your account if you forget your password.")
	key = _create_key()
	user_data["key_hash1"] = _string_hash(key, _mod1)
	user_data["key_hash2"] = _string_hash(key, _mod2)  #get and save the hash of key
	print("Your key is: " + key)
	user_data["activation"] = True #register complete

def _login_account():
	password= input("Please enter your password:")
	hash1 = _string_hash(password, _mod1)
	hash2 = _string_hash(password, _mod2) #the hash value of password user input
	if hash1 == user_data["password_hash1"] and hash2 == user_data["password_hash2"]:
		print("Welcome back! " + user_data["name"])
		return True
	else:
		print("Wrong password!")
		return False

def _forget_password():
	key = input("Please enter your key:")
	hash1 = _string_hash(key, _mod1)
	hash2 = _string_hash(key, _mod2) #the hash value of key user input
	if hash1 == user_data["key_hash1"] and hash2 == user_data["key_hash2"]:
		password = input("Please enter your new password:")
		hash1 = _string_hash(password, _mod1)
		hash2 = _string_hash(password, _mod2)
		user_data["password_hash1"] = hash1
		user_data["password_hash2"] = hash2 #reset password
		print("Your password has been changed successfully!")
		return True
	else:
		print("Wrong key!")
		return False

def _cancel_account():
	check = input("Type \"yes\" to confirm, or just press Enter to cancel:")
	if check == "yes":
		user_data["activation"] = False  # change to unregister state
		print("Your account has been cancelled successfully!")
		return True
	return False

def login():
	if not user_data["activation"]:
		_register_account()  #check did the user register
	print(f"Hi, {user_data["name"]}!")
	res = 0 #the result of login
	while True: #loop until login success or exit
		print("1. Login")
		print("2. Forget password")
		print("3. Exit")
		print("4. Cancel account") #give user choices
		choice =  input("Please enter your choice:")
		if choice == "1":
			if _login_account():
				res = 1
				break #login success
		elif choice == "2":
			_forget_password()
		elif choice == "3":
			break #exit
		elif choice == "4":
			if _cancel_account():
				res = 2
				break
		else :
			print("Invalid choice!")
	json_operate.save_json("user_data.json", user_data) #save the change of user data
	return res