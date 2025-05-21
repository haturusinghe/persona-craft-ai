# PersonaCraft.AI

PersonaCraft.AI is a comprehensive machine learning platform that crawls, processes, and transforms digital content from various sources into high-quality instruction and preference datasets for training AI models. The system creates personalized AI training data by analyzing an individual's digital footprint across multiple platforms.

## 🚀 Features

- **Multi-Platform Data Crawling**: Automated extraction from LinkedIn profiles, Medium articles, GitHub repositories, and custom web articles
- **Intelligent Data Processing**: Advanced text cleaning, chunking, and embedding generation using sentence transformers
- **Dataset Generation**: Creates both instruction-following and preference datasets using OpenAI GPT models
- **MLOps Pipeline**: Built with ZenML for reproducible machine learning workflows
- **Vector Database Integration**: Qdrant for efficient similarity search and retrieval
- **Data Warehouse**: MongoDB for structured data storage
- **Automated Publishing**: Direct integration with Hugging Face Hub for dataset sharing

## 🏗️ Architecture

The system follows a modular, pipeline-based architecture:

1. **Data Extraction Layer**: Selenium-based crawlers for different platforms
2. **Data Processing Layer**: Text cleaning, chunking, and embedding generation
3. **Feature Engineering**: Vector database storage and retrieval augmented generation (RAG)
4. **Dataset Generation**: LLM-powered creation of training datasets
5. **Publishing Layer**: Automated dataset validation and publishing

## 🛠️ Tech Stack

- **Backend**: Python 3.11, FastAPI
- **ML Pipeline**: ZenML, LangChain
- **Data Storage**: MongoDB, Qdrant Vector Database
- **ML Models**: OpenAI GPT-4, Sentence Transformers
- **Web Scraping**: Selenium, BeautifulSoup4
- **Containerization**: Docker, Docker Compose
- **Package Management**: Poetry

## 📦 Installation

1. Install dependencies:
    - Partial installation (excluding AWS-related packages):  
      ```bash
      poetry install --without aws
      ```
    - Full installation (all dependencies):  
      ```bash
      poetry install
      ```

2. Install Poe the Poet plugin (one-time per system):  
    ```bash
    poetry self add 'poethepoet[poetry_plugin]'
    ```

3. Test Poe with a sample task:
    - Run the task:  
      ```bash
      poetry poe run-sample-hello
      ```
    - Expected output:  
      ```
      hello poe is working
      ```

## Using the Virtual Environment

Poetry 2.0+ does not enable `poetry shell` by default. You can activate the virtual environment manually:

```bash
source $(poetry env info --path)/bin/activate
```
Once inside the activated environment, you can run Poe tasks directly with:
```bash
poe run-sample-hello
```

## 🚀 Quick Start

### 1. Start Infrastructure Services
```bash
docker-compose up -d
```

### 2. Run Complete Pipeline
```bash
# Extract data from digital platforms
poetry poe run-digital-data-etl --user "John Doe" --links "https://linkedin.com/in/johndoe,https://medium.com/@johndoe"

# Process and generate embeddings
poetry poe run-feature-engineering --authors "John Doe"

# Generate training datasets
poetry poe run-generate-datasets --dataset-type instruction --push-to-hf --dataset-id "your-org/dataset-name"
```

## 📊 Pipeline Overview

### 1. Digital Data ETL Pipeline
- **Input**: User profile links (LinkedIn, Medium, GitHub, custom articles)
- **Process**: Automated crawling and data extraction
- **Output**: Raw documents stored in MongoDB

### 2. Feature Engineering Pipeline
- **Input**: Raw documents from data warehouse
- **Process**: Text cleaning, chunking, embedding generation
- **Output**: Vector embeddings stored in Qdrant

### 3. Dataset Generation Pipeline
- **Input**: Processed documents and embeddings
- **Process**: LLM-powered generation of instruction/preference pairs
- **Output**: Formatted datasets ready for model training

## 🎯 Use Cases

- **Personal AI Assistants**: Train models that understand and mimic specific writing styles
- **Content Generation**: Create AI models specialized in particular domains or expertise areas
- **Educational AI**: Develop tutoring systems based on expert knowledge
- **Research**: Generate synthetic datasets for training domain-specific language models

## 🔧 Configuration

Key environment variables:
```bash
# OpenAI API (required for dataset generation)
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL_ID=gpt-4o-mini

# Hugging Face (for dataset publishing)
HUGGINGFACE_ACCESS_TOKEN=your_hf_token

# Database connections
DATABASE_HOST=mongodb://persona_craft_ai:persona_craft_ai@127.0.0.1:27017
QDRANT_DATABASE_HOST=localhost
QDRANT_DATABASE_PORT=6333
```

## 📁 Project Structure

```
persona_craft_ai/
├── application/           # Core application logic
│   ├── crawlers/         # Platform-specific data extractors
│   ├── dataset/          # Dataset generation and processing
│   ├── networks/         # ML model interfaces
│   └── preprocessing/    # Data cleaning and transformation
├── domain/               # Business logic and data models
├── infrastructure/       # Database and external service integrations
pipelines/                # ZenML pipeline definitions
steps/                    # Individual pipeline steps
tools/                    # CLI and utility scripts
```

## 📈 Dataset Types

### Instruction Datasets
Perfect for supervised fine-tuning of language models:
```json
{
  "instruction": "Explain the concept of vector embeddings in machine learning",
  "answer": "Vector embeddings are dense numerical representations..."
}
```

### Preference Datasets
Ideal for RLHF (Reinforcement Learning from Human Feedback):
```json
{
  "instruction": "Describe best practices for API design",
  "chosen": "High-quality extracted response from expert content",
  "rejected": "Generated alternative response"
}
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

For questions and support, please open an issue in the GitHub repository.
