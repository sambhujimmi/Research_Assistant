# AI Research Assistant

This project is a smart research assistant that helps users search, summarize, and analyze research papers efficiently. It integrates with the arXiv API to fetch academic papers and uses GPT-powered summarization to provide quick insights into research topics. The telegram bot can also fetch top 5 academic papers from arXiv related to the message sent to it.

---

## Features

### Telegram bot

**Fetch Research Papers** – Get top 5 academic papers from **arXiv** by messaged topic.

### Web app

**Fetch Research Papers** – Search academic papers from **arXiv** by topic.  
**AI-Powered Summarization** – Summarizes abstracts for faster understanding.  
**Sorting & Filtering** – Sort results by **relevance, last update, or submission date**.  
**"More" Button** – Loads additional papers dynamically without reloading.  
**Beautiful UI** – Clean and responsive design for better readability.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/sambhujimmi/Research_Assistant.git
cd Research_Assistant
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate      # On Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up environment variables:

- Create a `.env` file
- Copy the contents of `env.example`
- Paste your API keys

---

## Usage

### Telegram interface

1. Telegram Agent:

```bash
python main_telegram.py
```

2. Search for research papers:

- Search for **"@code_busters_bot"** on telegram
- Message a research topic

### Web app

1. Start the flask app:

```bash
python app.py
```

2. Search for research papers:

- Open your browser and go to `http://127.0.0.1:5000/`.
- Enter a **research topic** in the search bar.
- Click **"Search"** to fetch papers from arXiv.

3.  Summarize Papers

- Click **"Summarize"** under any research paper to get a **GPT-powered summary** of

4. Load More Papers

- Click **"More"** to fetch additional papers dynamically.
