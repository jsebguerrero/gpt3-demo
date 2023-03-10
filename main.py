import openai 
import streamlit as st

# pip install streamlit-chat  
from streamlit_chat import message

openai.api_key = st.secrets["api_secret"]
def generate_response(prompt):
    completions = openai.Completion.create(
        model="ada:ft-personal-2023-03-10-19-55-26",
        prompt=prompt + '\n\n###\n\n',
        temperature=0.0,
        max_tokens=100,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0.0
        )
    message = completions.choices[0].text.strip()[0]
    return message
st.title("Demo GPT-3 Chatbot Conversational")

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

# We will get the user's input by calling the get_text function
def get_text():
    input_text = st.text_input("You: ","Hola, me dicen que eres el nuevo chatbot de Konecta, que puedes ofrecerle a una empresa de BPO como chatbot?", key="input")
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
