
import os
import general_tools
from google import genai
from google.genai import types

# Initialize Google Generative AI client with API key
client = genai.Client(api_key = os.environ["API_KEY"])

def ai_chat_menu():
	# Create a chat instance with Gemini model and custom system prompt
	chat = client.chats.create(
		model = "gemini-2.0-flash",
		config = types.GenerateContentConfig(system_instruction = general_tools.read_txt("AI_system_prompt.txt"))
	)
	while True:
		# Get user input and process it
		question = input("Please ask any question about your mental health (enter 0 to exit): ")
		if question == "0":
			break
		else:
			# Send message to AI and display response
			response = chat.send_message(question)
			print()
			print(response.text)