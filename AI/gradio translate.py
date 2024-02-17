import gradio as gr

demo = gr.load("Helsinki-NLP/opus-mt-ko-en", src="models").launch()
