import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.markdown("## THINK BIG.")

        st.markdown("### Analysis History")
        # Initialize history in session state if it doesn't exist
        if "history" not in st.session_state:
            st.session_state.history = []

        # Display history items
        if not st.session_state.history:
            st.caption("No Recent Analysis..")
        else:
            # Reverse the list to show newest first
            for item in reversed(st.session_state.history):
                color = "green" if item['label'] == "Positive" else "Red"
                st.markdown(
                    f"**:{color}[{item['label']}]**<br><small>{item['text'][:35]}...</small>",
                    unsafe_allow_html=True
                )
                st.caption("Model: BERT Sentiment<br>Status: Ready", unsafe_allow_html=True)