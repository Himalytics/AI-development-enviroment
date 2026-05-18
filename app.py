import gradio as gr

def welcome_user(name):
    if not name.strip():
        return "Please enter your name."
    return f"Hello {name}, welcome to my AI development environment!"

demo = gr.Interface(
    fn=welcome_user,
    inputs=gr.Textbox(label="Enter your name"),
    outputs=gr.Textbox(label="Welcome Message"),
    title="Hello World Development Environment",
    description="This simple Gradio application demonstrates a working development environment connected to Git-based version control."
)

if __name__ == "__main__":
    demo.launch()