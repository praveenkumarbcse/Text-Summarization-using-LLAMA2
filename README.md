# Text Summarization with AI Models

This repository contains Python scripts for text summarization using AI models provided by Google's Gemini AI and OpenAI's Ollama. These scripts enable summarization of text from a file or direct input using different AI-powered models.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
- [Usage](#usage)
  - [Gemini AI Script](#gemini-ai-script)
  - [Ollama AI Script](#ollama-ai-script)
- [Contact](#contact)

## Features

- **Gemini AI Script**:
  - Summarizes text using the Gemini AI model from Google.
  - Requires an API key for authentication.
  - Can process text from a file or direct input.

- **Ollama AI Script**:
  - Utilizes the Ollama model from OpenAI for text summarization.
  - Supports summarization of text from a file or direct input.
  - Offers flexibility with model selection (`llama2`, `mistral`, etc.).

## Installation

### Prerequisites

- Python 3.8 and above installed
- Dependencies listed in `requirements.txt`

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/praveenkumarbcse/Text-Summarization-using-LLAMA2.git
   cd Text-Summarization-using-LLAMA2
2. **Install required dependencies:**

	```bash
	pip install -r requirements.txt
3. **Set up environment variables:**

	```For Gemini AI script: Obtain an API key from Google and set it in a .env file:
	makefile
	API_KEY=your_api_key_here
	For Ollama AI script: No additional environment variables required.

### Usage
#### Gemini AI Script
**Run the Gemini AI script with:**
	
	cd Gemini
	python text_summarization_using_gemini_api.py -t <path_to_text_file>   # Summarize text from a file
	python text_summarization_using_gemini_api.py -i "Your direct input"   # Summarize direct input
#### Ollama AI Script
**Run the Ollama AI script with:**
	
	cd ollama
	python text_summarization_using_ollama_llama2.py -t <path_to_text_file>   # Summarize text from a file
	python text_summarization_using_ollama_llama2.py -i "Your direct input"   # Summarize direct input
Contributing
Contributions are welcome! Please fork the repository and create a pull request with your improvements.

### Acknowledgments

* Google Gemini AI
* OpenAI Ollama

## Contact

For any questions or feedback, feel free to contact the maintainer:

* **Name:** Praveenkumar B.
* **Email:** praveenkumarbcse@gmail.com
