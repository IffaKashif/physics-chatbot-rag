import gradio as gr

# 🧠 Real chatbot function using your `qa_chain`
def chatbot_response(user_input):
    try:
        response = qa_chain.invoke({"query": user_input})
        return response["result"]
    except Exception as e:
        return f"❌ Error: {str(e)}"

# 🎨 Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## 📘 Physics Chatbot (LangChain + GPT-2 + FAISS)")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(placeholder="Type your physics question here...", label="Your Message")
    clear = gr.Button("🧹 Clear Chat")

    def respond(message, chat_history):
        answer = chatbot_response(message)
        chat_history.append((message, answer))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: [], None, chatbot, queue=False)

demo.launch()