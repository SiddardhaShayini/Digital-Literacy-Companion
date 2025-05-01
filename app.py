import streamlit as st
import time
from chatbot import process_query, get_initial_message
from data.topics import get_topics
from data.resources import get_resources
from utils import clean_user_input

# Page configuration
st.set_page_config(
    page_title="Digital Literacy Companion",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state variables
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'feedback_given' not in st.session_state:
    st.session_state.feedback_given = set()

# Sidebar with app information and topic selection
with st.sidebar:
    st.title("Digital Literacy Companion")
    st.markdown("### Your friendly guide to the digital world")
    
    st.markdown("---")
    st.markdown("### Topics I Can Help With:")
    topics = get_topics()
    
    for category, topic_list in topics.items():
        with st.expander(f"📚 {category}"):
            for topic in topic_list:
                if st.button(topic, key=f"topic_{topic}", use_container_width=True):
                    user_input = topic
                    st.session_state.chat_history.append({"role": "user", "content": user_input})
                    with st.spinner("Thinking..."):
                        time.sleep(0.5)  # Add a slight delay for better UX
                        response = process_query(user_input)
                    st.session_state.chat_history.append({"role": "assistant", "content": response})
                    st.rerun()
    
    st.markdown("---")
    st.markdown("### Additional Resources")
    with st.expander("📋 Helpful Resources"):
        resources = get_resources()
        for category, resource_list in resources.items():
            st.markdown(f"**{category}**")
            for resource in resource_list:
                st.markdown(f"- [{resource['title']}]({resource['url']})")
    
    st.markdown("---")
    if st.button("Clear Chat History", use_container_width=True):
        st.session_state.chat_history = []
        st.session_state.feedback_given = set()
        st.rerun()

# Main chat interface
st.title("Digital Literacy Companion 💬")
st.markdown("**Hello!** I'm here to help you navigate the digital world with confidence. Ask me any question about technology, social media, online safety, or any digital topic!")

# Display chat history
for i, message in enumerate(st.session_state.chat_history):
    if message["role"] == "user":
        st.markdown(f"<div style='background-color: #f0f2f6; padding: 10px; border-radius: 10px; margin-bottom: 10px;'><strong>You:</strong> {message['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='background-color: #e1f5fe; padding: 10px; border-radius: 10px; margin-bottom: 10px;'><strong>Assistant:</strong> {message['content']}</div>", unsafe_allow_html=True)
        
        # Add feedback buttons if feedback not already given for this message
        if i not in st.session_state.feedback_given:
            col1, col2, col3 = st.columns([1, 1, 8])
            with col1:
                if st.button("👍 Helpful", key=f"helpful_{i}"):
                    st.session_state.feedback_given.add(i)
                    st.toast("Thank you for your feedback!")
                    st.rerun()
            with col2:
                if st.button("👎 Not Helpful", key=f"not_helpful_{i}"):
                    st.session_state.feedback_given.add(i)
                    st.toast("I'll try to improve my answers. Thanks for letting me know!")
                    st.rerun()

# Display initial message if chat history is empty
if not st.session_state.chat_history:
    st.markdown(f"<div style='background-color: #e1f5fe; padding: 15px; border-radius: 10px; margin: 20px 0;'><strong>Assistant:</strong> {get_initial_message()}</div>", unsafe_allow_html=True)

# Chat input
user_input = st.chat_input("Type your question here...")

if user_input:
    # Clean the input
    cleaned_input = clean_user_input(user_input)
    
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": cleaned_input})
    
    # Get chatbot response with a loading spinner
    with st.spinner("Thinking..."):
        time.sleep(0.5)  # Add a slight delay for better UX
        response = process_query(cleaned_input)
    
    # Add chatbot response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": response})
    
    # Force a rerun to update the display
    st.rerun()

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>Digital Literacy Companion - Helping you navigate the digital world with confidence.</div>", unsafe_allow_html=True)
