import gradio as gr
# from retriever import retrieve_answer
import sys
sys.path.append("E:/Training/Atomcamp/DS6_Bootcamp/Projects/FYP/fyp-chatbot")
import gradio as gr
# from src.main import retriever
from src.retriever import retrieve_answer_from_docs

# Create the chatbot interface
def create_chat_interface():
    # Create an empty list to store chatbot messages
    messages = []

    # Add initial instructions or welcome message
    messages.append(("Hello! How can I help you today?", "KIU-bot"))

    # Create Gradio chatbot with the messages list
    chatbot = gr.Chatbot(value=messages)

    # Create Gradio interface
    interface = gr.ChatInterface(
        fn=retrieve_answer_from_docs,  # retriever
        chatbot=chatbot,
        title="university-rules-chatbot",
        description="Ask any question related to Karakoram International University Gilgit-Baltistan.",
        examples=[["What courses does KIU offer?"]]
    )

    return interface

# Function to launch the chatbot
def launch_chatbot():
    interface = create_chat_interface()
    interface.launch(debug=True)  # , share=True

if __name__ == "__main__":
    launch_chatbot()
