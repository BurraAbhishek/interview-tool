import streamlit as st
from openai import OpenAI


def evaluate_candidate():

    st.write("Thank you for your time! We will provide your feedback shortly...")

    if not st.session_state.feedback_shown:

        st.subheader("Feedback", divider="rainbow")

        conversation_history = "\n".join(
            [f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages]
            )
        
        feedback_client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

        feedback_prompt = """
            You are a helpful tool that evaluates an interviewee's performance based on the given context.
            
            Evaluate the user's responses. Give an overall score from 0 to 100.

            Remember that a rating from 0 to 49 renders the candidate unlikely to be considered for the position. 
            A rating from 50 to 69 indicate a slim chance of the interviewee being hired. 
            From 70 to 89, they are considered a promising candidate and a top contender above 90.

            Before the feedback, give the score.

            Follow this format:
            Overall Score: //Your score / 100
            Feedback: //Here you put your feedback

            Give only the feedback. Do not ask any additional questions.
        """

        feedback_response = feedback_client.responses.create(
            model=st.session_state["openai_model"],
            input=[
                {
                    "role": "system",
                    "content": feedback_prompt
                },
                {
                    "role": "user",
                    "content": f"This is the interview you need to evaluate. Keep in mind that you are only a tool. And you shouldn't engage in any further conversation. Here is the interview: {conversation_history}"
                }
            ]
        )

        feedback_value = feedback_response.output_text

        st.write(feedback_value)
