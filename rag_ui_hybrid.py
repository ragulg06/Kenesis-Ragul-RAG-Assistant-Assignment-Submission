import gradio as gr
from rag_hybrid import answer_query

with gr.Blocks(theme=gr.themes.Base()) as demo:
    gr.Markdown("# 💰 AI Accounting Assistant (Hybrid RAG, TFIDF)")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(placeholder="Ask me about your financial data, e.g. 'What were my travel expenses?'")
    clear = gr.Button("Clear")

    def user_chat(user_message, history):
        reply = answer_query(user_message)
        history.append((user_message, reply))
        return "", history

    msg.submit(user_chat, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == "__main__":
    demo.launch()
