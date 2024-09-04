import streamlit as st
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from chain import load_normal_chain
from sidebar_contents import write_sidebar_contents

bg_settings = """
<style>
[data-testid="stAppViewContainer"]{
background-image: linear-gradient(to right, #b2b1e2, #b4b7e8, #b6beed, #b8c4f2, #bacaf7, #b6d0fb, #b3d6fd, #b1dcff, #ace3fe, #ace9fa, #b1eef5, #b9f3ef);
}
[data-testid="stHeader"]{
    background-color: rgba(0,0,0,0);
}
[data-test_id="stApp"]{
    background-color: white;
}
</style>
"""


def set_send_input():
    st.session_state.send_input = True
    st.session_state.user_question = st.session_state.user_input
    st.session_state.user_input = ""
def load_chain(chat_history):
    return load_normal_chain(chat_history)


def main():
    # Webapp configurations
    st.set_page_config(page_title="PrepAI", page_icon="📖", layout="centered")
    st.title("PrepAI : Your guide for interview preparation.")
    st.markdown(bg_settings, unsafe_allow_html=True)
    write_sidebar_contents()
    # Designing the app
    chat_container = st.container()
    chat_history = StreamlitChatMessageHistory(key="history")
    if "send_input" not in st.session_state:
        st.session_state.send_input = False
        st.session_state.user_question = ""

    user_input = st.text_input("Type your reply here ", key="user_input", on_change=set_send_input)
    send_button = st.button("Send", key="send_button")

    llm_chain = load_chain(chat_history)
    if send_button or st.session_state.send_input:
        if st.session_state.user_question != "":
            with chat_container:
                llm_chain.run(st.session_state.user_question)
                st.session_state.user_question = ""
                st.divider()

    if chat_history.messages != []:
        with chat_container:
            st.write("Session so far")
            for message in chat_history.messages:
                st.chat_message(message.type).write(message.content)


if __name__ == "__main__":
    main()
