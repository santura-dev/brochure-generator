"""Main application entry point."""

from src.gradio_interface import GradioInterface

def main():
    interface = GradioInterface()
    interface.launch()

if __name__ == "__main__":
    main()