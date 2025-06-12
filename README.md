# Brochure Generator

A professional marketing content generator that automatically creates company brochures by analyzing website content using AI. Built with Python and LLMs, it features real-time generation progress, multi-language support, and a clean web interface.

## Features

- **Web Scraping**: Uses BeautifulSoup to extract content and links from company websites
- **LLM Integration**: Leverages local or cloud LLMs to generate professional marketing content
- **Streaming Output**: Displays the brochure generation in real-time with a typewriter effect
- **Translation**: Translates generated content while preserving formatting and tone
- **Web Interface**: Clean Gradio UI for easy interaction and progress tracking
- **Modular Design**: Clean, well-documented code organized for easy extension

## Prerequisites

- Python 3.8+
- A local LLM server (e.g., Ollama) or OpenAI API access
- VS Code or another Python IDE
- Git for version control

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/santura-dev/brochure-generator.git
   cd brochure-generator
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**

   ```bash
   # Optional: Create .env file if using OpenAI API
   OPENAI_API_KEY=your-api-key
   ```

5. **Start Local LLM (if using Ollama)**
   ```bash
   ollama serve
   ```

## Usage

1. Start the web interface:

   ```bash
   python -m src.app
   ```

2. In the interface:
   - Enter company name and website URL
   - Optionally specify a target language for translation
   - Click "Generate Brochure" to start the process
   - Watch real-time progress in the status area

## Dependencies

- `requests`: Web scraping
- `beautifulsoup4`: HTML parsing
- `openai`: LLM integration
- `python-dotenv`: Environment management
- `gradio`: Web interface

## Notes

- Supports both local LLMs and OpenAI's API
- Some websites may block scraping; ensure compliance with terms of service
- Translation quality depends on the LLM's language capabilities

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with improvements or bug fixes.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
