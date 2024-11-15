import streamlit as st
from openai import OpenAI
# Initialize the OpenAI client with your API key
myclient = OpenAI(
    base_url= "http://localhost:11434/v1",
    api_key= "ollama"
    )

def get_completion(user_prompt, text_to_process, model="Eomer/gpt-3.5-turbo:latest"):
    full_prompt = f"{user_prompt} '''{text_to_process}'''"
    messages = [{"role": "user", "content": full_prompt}]
    try:
        # Using the OpenAI Client to create a completion
        response = myclient.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0
        )
        return response.choices[0].message.content
    except Exception as e:
        # Return the error message if something goes wrong
        return f"An error occurred: {str(e)}"

# Streamlit interface setup
st.title('AI Text Processing App')

# Dropdown menu to select the model
model_choice = st.selectbox(
    "Choose a model:",
    ["Eomer/gpt-3.5-turbo:latest", "llama3.2"],
    index=0
)

# Text area for entering the custom prompt
custom_prompt = st.text_area("Enter your prompt:", height=100, help="Type the prompt to guide the AI.")

# Text area for user input to be processed
text_to_process = st.text_area("Enter your text here:", height=300, help="Type the text you want the AI to process according to the prompt.")

# Button to trigger processing
if st.button('Process Text'):
    # Get the response from the model
    response = get_completion(custom_prompt, text_to_process, model=model_choice)
    # Display the processed text
    st.text_area("Processed Text:", response, height=150)
