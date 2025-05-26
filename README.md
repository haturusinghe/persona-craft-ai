# PersonaCraft.AI

PersonaCraft.AI is a comprehensive machine learning platform that crawls, processes, and transforms digital content from various sources into high-quality instruction and preference datasets for training AI models. The system creates personalized AI training data by analyzing an individual's digital footprint across multiple platforms.

## 🚀 Features

- **Multi-Platform Data Crawling**: Automated extraction from LinkedIn profiles, Medium articles, GitHub repositories, and custom web articles
- **Intelligent Data Processing**: Advanced text cleaning, chunking, and embedding generation using sentence transformers
- **Dataset Generation**: Creates both instruction-following and preference datasets using OpenAI GPT models
- **Model Fine-tuning**: Supports both Supervised Fine-Tuning (SFT) and Direct Preference Optimization (DPO) training
- **MLOps Pipeline**: Built with ZenML for reproducible machine learning workflows
- **Vector Database Integration**: Qdrant for efficient similarity search and retrieval
- **Data Warehouse**: MongoDB for structured data storage
- **Cloud Training**: AWS SageMaker integration for scalable model training
- **Automated Publishing**: Direct integration with Hugging Face Hub for dataset and model sharing

## 🏗️ Architecture

The system follows a modular, pipeline-based architecture:

1. **Data Extraction Layer**: Selenium-based crawlers for different platforms
2. **Data Processing Layer**: Text cleaning, chunking, and embedding generation
3. **Feature Engineering**: Vector database storage and retrieval augmented generation (RAG)
4. **Dataset Generation**: LLM-powered creation of training datasets
5. **Model Training**: SFT and DPO fine-tuning pipelines with cloud support
6. **Publishing Layer**: Automated dataset and model validation and publishing

## 🛠️ Tech Stack

- **Backend**: Python 3.11, FastAPI
- **ML Pipeline**: ZenML, LangChain
- **Data Storage**: MongoDB, Qdrant Vector Database
- **ML Models**: OpenAI GPT-4, Sentence Transformers, Llama 3.1
- **Training**: TRL (Transformers Reinforcement Learning), Unsloth
- **Web Scraping**: Selenium, BeautifulSoup4
- **Cloud Platform**: AWS SageMaker
- **Containerization**: Docker, Docker Compose
- **Package Management**: Poetry
- **Monitoring**: Comet ML, Opik

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
# Start MongoDB and Qdrant databases
poetry poe local-infrastructure-up
```

### 2. Configure Environment
Set up your environment variables in `.env` file or export them:
```bash
export OPENAI_API_KEY="your_openai_api_key"
export HUGGINGFACE_ACCESS_TOKEN="your_hf_token"
```

### 3. Run Individual Pipelines

#### Extract Digital Data
```bash
# Run ETL for specific person configurations
poetry poe run-digital-data-etl-person1
poetry poe run-digital-data-etl-person2

# Or run both
poetry poe run-digital-data-etl
```

#### Process and Generate Embeddings
```bash
poetry poe run-feature-engineering-pipeline
```

#### Generate Training Datasets
```bash
# Generate instruction datasets for SFT
poetry poe run-generate-instruct-datasets-pipeline

# Generate preference datasets for DPO
poetry poe run-generate-preference-datasets-pipeline
```

#### Run Complete Data Pipeline
```bash
# Run all data pipelines in sequence
poetry poe run-end-to-end-data-pipeline
```

#### Train Models
```bash
# Train locally (requires GPU)
poetry run python -m tools.run --run-training

# Train on AWS SageMaker
python -m persona_craft_ai.model.finetuning.sagemaker
```

### 4. Stop Infrastructure
```bash
poetry poe local-infrastructure-down
```

## 🔧 CLI Commands

The project provides a comprehensive CLI through Poe the Poet tasks:

### Infrastructure Management
```bash
# Start all local infrastructure (MongoDB, Qdrant, ZenML)
poetry poe local-infrastructure-up

# Stop all local infrastructure
poetry poe local-infrastructure-down

# Start only Docker services
poetry poe local-docker-infrastructure-up

# Stop Docker services
poetry poe local-docker-infrastructure-down
```

### Data Pipeline Commands
```bash
# Run ETL for different personas
poetry poe run-digital-data-etl-person1
poetry poe run-digital-data-etl-person2
poetry poe run-digital-data-etl  # Runs both

# Feature engineering
poetry poe run-feature-engineering-pipeline

# Dataset generation
poetry poe run-generate-instruct-datasets-pipeline
poetry poe run-generate-preference-datasets-pipeline

# Complete data pipeline
poetry poe run-end-to-end-data-pipeline
```

### Direct CLI Access
```bash
# Access the main CLI with all options
poetry run python -m tools.run --help

# Available flags:
# --run-etl                    # Run ETL pipeline
# --run-feature-engineering    # Run feature engineering
# --run-generate-instruct-datasets     # Generate instruction datasets
# --run-generate-preference-datasets   # Generate preference datasets
# --run-end-to-end-data       # Run complete data pipeline
# --run-training              # Run model training
# --export-settings           # Export settings to ZenML
# --no-cache                  # Disable pipeline caching
```

## 📊 Pipeline Overview

### 1. Digital Data ETL Pipeline
- **Input**: User profile links (LinkedIn, Medium, GitHub, custom articles)
- **Process**: Automated crawling and data extraction using Selenium
- **Output**: Raw documents stored in MongoDB
- **Configuration**: Configured via YAML files in `configs/` directory

### 2. Feature Engineering Pipeline
- **Input**: Raw documents from data warehouse
- **Process**: Text cleaning, chunking, embedding generation using sentence transformers
- **Output**: Vector embeddings stored in Qdrant for similarity search

### 3. Dataset Generation Pipeline
- **Input**: Processed documents and embeddings
- **Process**: LLM-powered generation of instruction/preference pairs using RAG
- **Output**: Formatted datasets ready for model training
- **Types**: Instruction datasets (SFT) and preference datasets (DPO)

### 4. Training Pipeline
- **Input**: Generated datasets from Hugging Face
- **Process**: Fine-tuning using SFT and/or DPO methods
- **Models**: Based on Llama 3.1-8B architecture
- **Output**: Trained models published to Hugging Face Hub
- **Deployment**: Supports local training and AWS SageMaker

## 🧠 Model Training

PersonaCraft.AI supports two main training paradigms:

### Supervised Fine-Tuning (SFT)
- **Base Model**: Llama 3.1-8B
- **Method**: Instruction-following fine-tuning using LoRA
- **Dataset**: Generated instruction-output pairs from digital content
- **Output**: `PersonaCraftAILlama-3.1-8B` model

### Direct Preference Optimization (DPO)
- **Base Model**: SFT-trained PersonaCraft model
- **Method**: Preference-based alignment training
- **Dataset**: Preference pairs with chosen/rejected responses
- **Output**: `PersonaCraftAILlama-3.1-8B-DPO` model

### Training Options

#### Local Training
```bash
# SFT training
poetry run python -m tools.run --run-training

# Configure training parameters in configs/training.yaml
```

#### AWS SageMaker Training
```bash
# Cloud training with GPU instances
python -m persona_craft_ai.model.finetuning.sagemaker

# Supports ml.g5.2xlarge instances with automatic scaling
```

### Training Features
- **Efficient Training**: Uses Unsloth for 2x faster training with reduced memory usage
- **Monitoring**: Integrated with Comet ML for experiment tracking
- **Automatic Publishing**: Models are automatically pushed to Hugging Face Hub
- **Flexible Configuration**: Support for different model sizes and training parameters
- **Memory Optimization**: 4-bit quantization and LoRA for efficient training

## 🎯 Use Cases

- **Personal AI Assistants**: Train models that understand and mimic specific writing styles and expertise
- **Content Generation**: Create AI models specialized in particular domains or professional areas
- **Educational AI**: Develop tutoring systems based on expert knowledge and teaching styles
- **Research**: Generate synthetic datasets for training domain-specific language models
- **Corporate Training**: Create company-specific AI assistants based on internal expertise and documentation
- **Professional Development**: Build AI coaches that understand specific career paths and skills

## 🔧 Configuration

### Environment Variables
```bash
# OpenAI API (required for dataset generation)
OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL_ID=gpt-4o-mini

# Hugging Face (for dataset and model publishing)
HUGGINGFACE_ACCESS_TOKEN=your_hf_token

# Database connections
DATABASE_HOST=mongodb://persona_craft_ai:persona_craft_ai@127.0.0.1:27017
QDRANT_DATABASE_HOST=localhost
QDRANT_DATABASE_PORT=6333

# AWS SageMaker (optional, for cloud training)
AWS_ARN_ROLE=your_aws_sagemaker_role
AWS_REGION=us-east-1

# Monitoring (optional)
COMET_API_KEY=your_comet_api_key
COMET_PROJECT=your_project_name
```

### Pipeline Configuration
Pipeline configurations are managed through YAML files in the `configs/` directory:
- `digital_data_person_1.yaml` - ETL configuration for first persona
- `feature_engineering.yaml` - Feature engineering pipeline settings
- `generate_instruct_datasets.yaml` - Instruction dataset generation
- `generate_preference_datasets.yaml` - Preference dataset generation
- `training.yaml` - Model training configuration

### ZenML Settings
Export your settings to ZenML:
```bash
poetry run python -m tools.run --export-settings
```

## 📁 Project Structure

```
persona_craft_ai/
├── application/           # Core application logic
│   ├── crawlers/         # Platform-specific data extractors (LinkedIn, Medium, GitHub)
│   ├── dataset/          # Dataset generation and processing
│   ├── networks/         # ML model interfaces and embeddings
│   └── preprocessing/    # Data cleaning and transformation
├── domain/               # Business logic and data models
├── infrastructure/       # Database and external service integrations
│   └── db/              # MongoDB and Qdrant clients
├── model/                # Model training and fine-tuning
│   └── finetuning/      # SFT and DPO training scripts
pipelines/                # ZenML pipeline definitions
├── digital_data_etl.py  # Data extraction pipeline
├── feature_engineering.py # Data processing pipeline
├── generate_datasets.py # Dataset generation pipeline
├── training.py          # Model training pipeline
└── end_to_end_data.py   # Complete data pipeline
steps/                    # Individual pipeline steps
├── etl/                 # Data extraction steps
├── feature_engineering/ # Data processing steps
├── generate_datasets/   # Dataset generation steps
└── training/           # Model training steps
tools/                    # CLI and utility scripts
configs/                  # Pipeline configuration files
```

## 📈 Dataset Types

### Instruction Datasets (SFT)
Perfect for supervised fine-tuning of language models:
```json
{
  "instruction": "Explain the concept of vector embeddings in machine learning",
  "output": "Vector embeddings are dense numerical representations that capture semantic meaning..."
}
```

### Preference Datasets (DPO)
Ideal for Direct Preference Optimization and RLHF:
```json
{
  "prompt": "Describe best practices for API design",
  "chosen": "High-quality extracted response from expert content showcasing detailed API design principles...",
  "rejected": "Generated alternative response with less comprehensive or lower-quality information"
}
```

Both dataset types are automatically published to Hugging Face Hub and can be used for:
- **SFT Training**: Teaching models to follow instructions and generate appropriate responses
- **DPO Training**: Aligning models with human preferences and improving response quality
- **Model Evaluation**: Benchmarking model performance on domain-specific tasks

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

For questions and support, please open an issue in the GitHub repository.

## 🚀 Getting Started Examples

### Example 1: Complete Workflow
```bash
# 1. Setup infrastructure
poetry install --without aws
poetry poe local-infrastructure-up

# 2. Configure environment
export OPENAI_API_KEY="your_key"
export HUGGINGFACE_ACCESS_TOKEN="your_token"

# 3. Run complete data pipeline
poetry poe run-end-to-end-data-pipeline

# 4. Generate both dataset types
poetry poe run-generate-instruct-datasets-pipeline
poetry poe run-generate-preference-datasets-pipeline

# 5. Train your model
poetry run python -m tools.run --run-training
```

### Example 2: Custom Person Data
```bash
# 1. Create your own config file in configs/
# 2. Configure ETL for your specific persona
poetry run python -m tools.run --run-etl --etl-config-filename your_config.yaml

# 3. Process the data
poetry poe run-feature-engineering-pipeline
```

### Example 3: Cloud Training
```bash
# 1. Configure AWS credentials and SageMaker role
export AWS_ARN_ROLE="your_sagemaker_role"

# 2. Run training on SageMaker
python -m persona_craft_ai.model.finetuning.sagemaker
```
