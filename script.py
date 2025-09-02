import streamlit as st 
import os 
from google import generativeai as genai
from dotenv import load_dotenv
import tiktoken 



# Create a single client object
# client = genai.Client()

#------------------------- SIMPLE CHAT SECTION --------------------------------
# Load the environment variables 
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash-latest')

def chat():
    chat_session = model.start_chat(history=[])
    print("Chat session started. Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Ending chat session. Goodbye!")
            break

        # Send the message and get a streaming response.
        try:
            response = chat_session.send_message(user_input, stream=True)
                
            # Print the model's response as it comes in.
            print("Gemini: ", end="")
            for chunk in response:
                print(chunk.text, end="")
            
            print("\n")
            
        except Exception as e:
            print(f"An error occurred: {e}")

# chat()

# ----------------------------------- Work on the streamlit app -------------------------------------------------------

st.title("Insights Mate")
st.write("Hello, Mustafa!")
st.file_uploader("Upload data", type=["csv", "txt"])
st.sidebar.header("Options")
max_tokens  = st.sidebar.slider("Max tokens", min_value=100, max_value=4096, value=1024)
st.write("Max tokens:", max_tokens)