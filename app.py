import streamlit as st
from components.introduction import render_introduction
from utils.interviewer import interview
from utils.evaluator import evaluate_candidate


st.set_page_config(
    page_title="Streamlit Chat",
    initial_sidebar_state="collapsed"
)
st.title("Interview Chatbot")

if "setup_complete" not in st.session_state:
    st.session_state.setup_complete = False
if "user_message_count" not in st.session_state:
    st.session_state.user_message_count = 0
if "feedback_shown" not in st.session_state:
    st.session_state.feedback_shown = False
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_complete" not in st.session_state:
    st.session_state.chat_complete = False
if "questions" not in st.session_state:
    st.session_state.questions = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o"

if not st.session_state.setup_complete:
    render_introduction()

def show_feedback():
    st.session_state["feedback_shown"] = True

def interview_precheck():
    return bool(
        st.session_state.setup_complete
        and not st.session_state.feedback_shown
        and not st.session_state.chat_complete
    )

def can_end_interview():
    return st.session_state.user_message_count >= 5


if interview_precheck():

    interview()

if can_end_interview():

    evaluate_candidate()