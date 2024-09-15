import sys
sys.path.append("E:/Training/Atomcamp/DS6_Bootcamp/Projects/FYP/fyp-chatbot")
import gradio as gr
from src.main import retriever

# Create an empty list to store chatbot messages
messages = []

# Add initial instructions or welcome message
messages.append(("Hello! How can I help you today?", "KIU-bot"))

# Create Gradio chatbot with the messages list
chatbot = gr.Chatbot(value=messages)

# Create Gradio interface
result = gr.ChatInterface(
    fn=retriever,
    chatbot=chatbot,
    title="university-rules-chatbot",
    description="Ask any question related to Karakoram International University Gilgit-Baltistan.",
    examples=[["What courses does KIU offer?"]]
)#.launch(debug=True)

if __name__ == "__main__":
    result.launch(debug=True)

