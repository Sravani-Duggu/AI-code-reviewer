import google.generativeai as genai
import streamlit as st
import time
#set up google generative ai (genai) API key
f = open("keys/gemini.txt")
key = f.read()

#configure the generative ai API keys
genai.configure(api_key=key)

#set page configuration for the streamlit app
st.set_page_config(page_title="AI Code Reviewer", page_icon="🤖", layout="wide")

#custom css for styling the page and enhancing the look
st.markdown(
    """
    <style>
    body {
        background-color: #f0f8ff;
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextArea>textarea {
        background-color: #f8f8f8;
        border: 1px solid #dcdcdc;
        padding: 15px;
        font-size: 14px;
        width: 100%;
        height: 250px;
    }
    .stTextArea textarea:focus {
        border-color: #4CAF50;
    }
    .stAlert {
        background-color: #e6f7ff;
        color: #1e3a8a;
    }
    .stMarkdown h2 {
        color: #2e8b57;
    }
    .response-box {
        background-color: #ffffff;
        border-radius: 8px;
        border: 1px solid #ddd;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .spinner {
        text-align: center;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True
)

#title and subtitle of the app
st.title("GenAI - python Code Reviewer 🤖")
st.subheader("Paste your Python code below, and receive expert feedback and suggestions.")

#input area for python code
user_prompt = st.text_area("Enter your Python Code here:", placeholder="Paste your code here...", height=250)

#add a button for code review and show a spinner during model processing
if st.button("Generate Review"):
    if user_prompt.strip() != "":
        with st.spinner("Reviewing your code... Please wait. 🕑"):
            try:
                #initialize the generative AI model
                model = genai.GenerativeModel("models/gemini-1.5-flash")
                ai_assistant = model.start_chat(history=[])

                #send user input code for review to the model
                response = ai_assistant.send_message(
                    f"Please review the following Python code for errors or improvements:\n\n{user_prompt}\n\nProvide detailed feedback, point out improvements, and suggest fixes if necessary."
                )

                #display the feedback and corrected code
                st.markdown("<h2>Review & Suggestions:</h2>", unsafe_allow_html=True)
                st.markdown(f"<div class='response-box'>{response.text}</div>", unsafe_allow_html=True)
                st.success("Review generated successfully!")

            except Exception as e:
                st.error(f"An error occured: {e}")

    else:
        st.warning("Please enter your Python code for review.")

#additional spacing and closing toches for the UI
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Footer (Optional)
st.markdown(
    """
    <footer style="text-align: center; padding: 15px; background-color: #f0f8ff; color: #555;">
        <p>Powered by <strong>Google Generative AI</strong> | Code Review App | Created with 💙</p>
    </footer>
    """, unsafe_allow_html=True
)