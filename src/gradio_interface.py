import gradio as gr
from .broshure_generator import create_brochure, translate_brochure

def create_interface():
    demo = gr.Interface(
        fn=process_brochure,
        inputs=[
            gr.Textbox(label="Company Name", placeholder="Enter the company name"),
            gr.Textbox(label="Website URL", placeholder="Enter the website URL"),
            gr.Textbox(label="Target Language (optional)", placeholder="Enter the target language")
        ],
        outputs=[
            gr.Markdown(label="Generated Brochure"),
            gr.Markdown(label="Translated Brochure")
        ],
        title="Company Brochure Generator",
        description="Generate professional brochures from company websites with optional translation",
        theme=gr.themes.Soft(),
        allow_flagging="never"
    )
    return demo

def process_brochure(name: str, url: str, lang: str) -> tuple[str, str]:
    try:
        brochure = create_brochure(name, url)
        translated = ""
        if lang.strip():
            translated = translate_brochure(brochure, lang)
        return brochure, translated
    except Exception as e:
        return f"Error: {str(e)}", ""

class GradioInterface:
    def __init__(self):
        self.interface = create_interface()

    def launch(self):
        self.interface.launch(
            share=False,
            inbrowser=True,
            server_name="0.0.0.0",
            server_port=7860
        )