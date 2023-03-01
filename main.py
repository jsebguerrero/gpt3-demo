import openai 
import streamlit as st

# pip install streamlit-chat  
from streamlit_chat import message

openai.api_key = st.secrets["api_secret"]
def generate_response(prompt):
    completions = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt + '\n\n###\n\n',
        temperature=0.5,
        max_tokens=300,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0.0
        )
    message = completions.choices[0].text
    return message
st.title("Demo GPT-3 Chatbot")

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# We will get the user's input by calling the get_text function
def get_text():
    input_text = st.text_input("You: ","Hello, rumour has it that you are the new chatbot engine for Konecta, what can you do for me?", key="input")
    return input_text

user_input = get_text()

if user_input:
    output = generate_response(user_input)
    # store the output 
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
