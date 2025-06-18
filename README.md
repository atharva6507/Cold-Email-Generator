# 🤖 AI-Powered Cold Email Generator

> **Intelligent Business Development Automation** - Transform job postings into compelling cold emails using advanced AI and semantic search

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.41.1-red.svg)](https://streamlit.io)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.12-green.svg)](https://langchain.com)
[![Groq](https://img.shields.io/badge/Groq-LLaMA--3.3--70B-orange.svg)](https://groq.com)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector--Store-purple.svg)](https://chromadb.com)

## 🎯 Project Overview

This project demonstrates a sophisticated **AI-driven business development pipeline** that automatically generates personalized cold emails by:

1. **Web Scraping** job postings from career pages
2. **Intelligent Job Extraction** using LLM-powered parsing
3. **Semantic Portfolio Matching** via vector embeddings
4. **Contextual Email Generation** with relevant case studies

The system showcases advanced NLP techniques, vector search capabilities, and intelligent prompt engineering to create highly targeted business outreach.

## 🏗️ Architecture & Technical Stack

### Core Technologies
- **🤖 LLM**: Groq's LLaMA-3.3-70B-Versatile (Enterprise-grade inference)
- **🔗 LangChain**: Advanced prompt orchestration and chain management
- **📊 Vector Database**: ChromaDB for semantic similarity search
- **🌐 Web Scraping**: LangChain WebBaseLoader for dynamic content extraction
- **🎨 Frontend**: Streamlit for intuitive web interface
- **🐍 Backend**: Python with async processing capabilities

### Advanced Features
- **Semantic Portfolio Matching**: Vector embeddings for skill-based project retrieval
- **Intelligent Text Processing**: Regex-based content cleaning and normalization
- **JSON Schema Validation**: Structured output parsing with error handling
- **Persistent Vector Storage**: ChromaDB for scalable similarity search

## 🚀 How It Works

### 1. **Web Content Ingestion**
```python
# Dynamic web scraping with content cleaning
loader = WebBaseLoader([url_input])
data = text_cleaner(loader.load().pop().page_content)
```

### 2. **Intelligent Job Extraction**
The system uses advanced prompt engineering to extract structured job data:

```python
prompt_extract = PromptTemplate.from_template("""
### SCRAPED TEXT FROM WEBSITE:
{page_data}
### INSTRUCTION:
Extract job postings and return JSON with: role, experience, skills, description
### VALID JSON (NO PREAMBLE):
""")
```

### 3. **Semantic Portfolio Matching**
Leverages ChromaDB vector embeddings to find relevant case studies:

```python
# Vector similarity search for skill matching
links = portfolio_instance.query_links(skills)
```

### 4. **Contextual Email Generation**
Generates personalized emails using extracted job data and matched portfolio items:

```python
prompt_email = PromptTemplate.from_template("""
### JOB DESCRIPTION:
{job_description}
### INSTRUCTION:
Write a professional cold email highlighting capabilities 
with portfolio examples: {link_list}
### EMAIL (NO PREAMBLE):
""")
```


## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- Groq API key (for LLaMA-3.3-70B access)

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/cold-email-generator.git
cd cold-email-generator
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
```bash
# Create .env file
echo "GROQ_API_KEY=your_groq_api_key_here" > .env
```

4. **Run the application**
```bash
cd app
streamlit run main.py
```

## 🎮 Usage

1. **Access the web interface**
2. **Enter a job posting URL** (e.g., company careers page)
3. **Click Submit** to process the content
4. **Review generated emails** with matched portfolio examples

### Example Input
```
https://jobs.nike.com/job/R-46197
```

### Example Output
```
Subject: Floor Manager Position - Retail Leadership Expertise

Dear Hiring Manager,

I'm reaching out regarding your Floor Manager (Coach) position at Nike Amsterdam. 
Our company specializes in retail leadership and team management solutions.

Based on your requirements for three years of retail experience and leadership 
capabilities, I'd like to highlight our relevant expertise:

• Team Leadership: [Portfolio Link] - Successfully managed 15+ retail teams
• Digital Literacy: [Portfolio Link] - Implemented technology-driven solutions
• Consumer Engagement: [Portfolio Link] - Enhanced customer experience programs

Would you be interested in discussing how our retail leadership solutions 
could support your Amsterdam location?

Best regards,
[Your Name]
```

## 🔧 Technical Deep Dive

### LangChain Integration
The project demonstrates advanced LangChain patterns:

- **Prompt Templates**: Structured, reusable prompts with variable injection
- **Output Parsers**: JSON schema validation with error handling
- **Chain Composition**: Modular pipeline design for maintainability

### Vector Search Implementation
```python
class Portfolio:
    def __init__(self, file_path="resource/my_portfolio.csv"):
        self.chroma_client = chromadb.PersistentClient("vectorstore")
        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")
    
    def query_links(self, skills):
        return self.collection.query(query_texts=skills, n_results=2)
```

### Text Processing Pipeline
```python
def clean_text(text):
    # Remove HTML tags, URLs, special characters
    text = re.sub(r'<[^>]*?>', '', text)
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    return ' '.join(text.split())
```
