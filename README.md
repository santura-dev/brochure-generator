Brochure Generator
This project generates a professional brochure for a company by scraping its website, identifying relevant pages, and using a local LLM to create a Markdown-formatted document. The brochure is suitable for prospective customers, investors, and recruits, highlighting company culture, customers, and career opportunities. Additionally, the project supports streaming output and translation of the brochure into other languages (e.g., Polish).
This project demonstrates skills in web scraping, API integration, LLM prompting, and Python development, making it a valuable addition to a portfolio or CV.
Features

Web Scraping: Uses BeautifulSoup to extract content and links from a company website.
LLM Integration: Leverages a local LLM (llama3.2) to identify relevant links and generate a brochure.
Streaming Output: Displays the brochure generation in real-time with a typewriter effect.
Translation: Translates the generated brochure into a specified language while preserving formatting and tone.
Modular Design: Clean, well-documented code organized for easy extension and maintenance.
Professional Documentation: Includes setup instructions and usage examples for GitHub sharing.


Prerequisites

Python 3.8+
A local LLM server (e.g., Ollama with llama3.2) running at http://localhost:11434/v1
VS Code or another Python-compatible IDE
Git for version control

Setup Instructions

Clone the Repository
git clone https://github.com/santura-dev/brochure_generator.git
cd brochure_generator


Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies
pip install -r requirements.txt


The .env file is optional if using a local LLM with default settings. If using an external API, add your API key:OPENAI_API_KEY=your-api-key



Run a Local LLM Server

Install Ollama and pull the llama3.2 model:ollama pull llama3.2


Start the Ollama server:ollama serve




Run the Script
python src/brochure_generator.py

The script generates a brochure for GeeksForGeeks, displays it in Markdown, and translates it into Polish.


Usage

Generate a Brochure: The script scrapes the specified website (default: https://www.geeksforgeeks.org), identifies relevant pages (e.g., About, Careers), and generates a Markdown brochure.
Stream Output: Uncomment the stream_brochure call in brochure_generator.py to enable real-time output.
Translate Brochure: The script automatically translates the brochure into Polish. Modify the language variable to translate into another language.
Customize: Edit the company_name and url variables in brochure_generator.py to generate a brochure for a different company.

Example Output
The script generates a brochure like this:
# Introduction to GeeksForGeeks
## Our Mission
At GeeksForGeeks, our mission is to democratize access to quality education...
## Our Culture
- Inclusive and Supportive: We believe in creating a positive community...
## Our Customers
- Learners of all ages and skill levels...
## Our Courses and Resources
- Programming languages (Python, Java, C++, JavaScript, etc.)...

The translated brochure retains the same structure in the target language (e.g., Polish).
Dependencies
See requirements.txt for a full list. Key dependencies include:

requests: For web scraping
beautifulsoup4: For HTML parsing
openai: For LLM integration
python-dotenv: For environment variable management
ipython: For Markdown display

Notes

The project assumes a local LLM server (llama3.2) is running. To use a different LLM or API (e.g., OpenAI), update the OpenAI client configuration and .env file.
Some websites may block scraping; ensure compliance with terms of service.
The translation feature requires a capable LLM that supports the target language.

Contributing
Contributions are welcome! Please open an issue or submit a pull request with improvements or bug fixes.
License
This project is licensed under the MIT License. See LICENSE for details.
