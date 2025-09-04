import streamlit as st


def complete_setup():
    if st.session_state["name"] == "":
        return
    if st.session_state["position"] == "":
        return
    if st.session_state["company"] == "":
        return
    st.session_state.setup_complete = True
    st.write("Setup complete. Starting interview...")


def render_introduction():

    if not st.session_state.setup_complete:

        if "name" not in st.session_state:
            st.session_state["name"] = ""
        if "experience" not in st.session_state:
            st.session_state["experience"] = ""
        if "skills" not in st.session_state:
            st.session_state["skills"] = ""

        st.subheader("Personal info", divider="rainbow")

        st.session_state["name"] = st.text_input(
            label = "Name",
            max_chars=64,
            placeholder="Enter your name"
        )

        st.session_state["experience"] = st.text_area(
            label="Experience",
            placeholder="Describe your work experience",
            max_chars=256
        )

        st.session_state["skills"] = st.text_area(
            label="Skills",
            placeholder="List your skills",
            max_chars=256
        )

        st.write(f"**Your name**: { st.session_state["name"] }")
        st.write(f"**Your experience**: { st.session_state["experience"] }")
        st.write(f"**Your skills**: { st.session_state["skills"] }")

        st.subheader("Company and Position", divider="rainbow")

        if "level" not in st.session_state:
            st.session_state["level"] = "Entry-level"
        if "position" not in st.session_state:
            st.session_state["position"] = ""
        if "company" not in st.session_state:
            st.session_state["company"] = ""

        col1, col2 = st.columns(2)
        with col1:
            st.session_state["level"] = st.radio(
                "Choose level",
                key="visibility",
                options=["Entry-level", "Junior", "Mid-level", "Senior"]
            )

        with col2:
            st.session_state["position"] = st.text_input(
                label="Position",
                placeholder="Describe your target position"
            )

        st.session_state["company"] = st.text_input(
            label="Company",
            placeholder="Enter your target company"
        )

        st.write(f"**Target role**: {st.session_state["level"]} {st.session_state["position"]} at {st.session_state["company"]}")

        st.button("Start Interview", on_click=complete_setup)
