import os
import general_tools
from google import genai
from google.genai import types
client = genai.Client(api_key = os.environ["api_key"])

def ai_chat_menu():
	chat = client.chats.create(
		model = "gemini-2.0-flash",
		config = types.GenerateContentConfig(system_instruction = general_tools.read_txt("AI_system_prompt.txt"))
	)
	while True:
		question = input("Please ask any question about your mental health (enter 0 to exit): ")
		if question == "0":
			break
		else:
			response = chat.send_message(question)
			print()
			print(response.text)