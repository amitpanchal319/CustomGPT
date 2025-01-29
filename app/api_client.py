

import os
from groq import Groq
from logger import CustomLogger 
from dotenv import load_dotenv

# Load environment variables from .env file

load_dotenv()

class GroqClient:
    # Class to interact with the groq api

    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.client = Groq(api_key=self.api_key)
        self.logger = CustomLogger().get_logger()

    def get_response(self, messages):
        """ Send message to the Groq API and return the response.
        : param messages: List of messages for the conversation.
        : return: AI response as a string. """

        try:
            self.logger.info("Sending messages to Groq API...")
            chat_completion = self.client.chat.completions.create(
                messages = messages,
                model="llama3-8b-8192"  # Use the appropriate model for general use
            )
            response = chat_completion.choices[0].message.content
            self.logger.info("Received response from Groq API.")
            return response
        
        except Exception as e:
            self.logger.error(f"Error communicating with Groq API: {e}")
        return "Sorry, I couldn't get a response at this time."