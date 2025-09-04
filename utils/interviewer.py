import streamlit as st
from openai import OpenAI


def can_end_interview():
    return st.session_state.user_message_count >= 5


def interview():

    client = OpenAI(api_key=st.secrets.get("OPENAI_API_KEY"))

    if not st.session_state.messages:
        questions = []
        history = []
        system_message = f"""
        You are an HR Executive for the company {st.session_state["company"]} interviewing a candidate named {st.session_state["name"]} for the position {st.session_state["level"]} {st.session_state["position"]}. 
        The candidate has the following experience: {st.session_state["experience"]}. 
        The candidate has the skills: {st.session_state["skills"]}. 
        Use this data to create some questions: {questions}. Ask questions one at a time.
        Chat history: {history}. 
        """
        st.session_state.messages = [{
            "role": "system",
            "content": system_message
        }]

    if not can_end_interview():

        st.info(
            """
            Start by introducing yourself!
            """
        )

        for i in st.session_state.messages:

            if i["role"] in ["user", "assistant"]:
                with st.chat_message(i["role"]):
                    st.markdown(i["content"])

        if prompt := st.chat_input("Your answer: ", max_chars=1024):

            prompt = str(prompt)

            client = OpenAI(api_key=st.secrets.get("OPENAI_API_KEY"))

            moderation = client.moderations.create(
                model="omni-moderation-latest",
                input=prompt
            )

            if moderation.results[0].flagged is False:

                st.session_state.messages.append({
                    "role": "user",
                    "content": prompt
                })

                with st.chat_message("user"):
                    st.markdown(prompt)

                with st.chat_message("assistant"):
                    stream = client.responses.create(
                        model = st.session_state["openai_model"],
                        input = [
                            {"role": m["role"], "content": m["content"]}
                            for m in st.session_state.messages
                        ],
                        stream=True
                    )
                    response = ""
                    placeholder = st.empty()
                    for i in stream:
                        if i.type == "response.output_text.delta":
                            response += i.delta
                            placeholder.write(response)
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": response
                    })
                    st.session_state.user_message_count += 1
        
    else:
        return
