# Mediora

## Mediora: An AI-Powered Medical Retrieval-Augmented Generation (RAG) Chatbot

### Overview:
I developed Mediora, an advanced Retrieval-Augmented Generation (RAG) chatbot engineered to deliver accurate and contextually rich responses derived from medical literature. The system seamlessly combines Flask, LangChain, HuggingFace Transformers, and FAISS to create a reliable, production-ready AI solution for healthcare information access.

### Key Highlights:

* Flask powers the interactive and user-friendly web interface.

* LangChain orchestrates the RAG workflow, integrating retrieval and generation for high-quality, evidence-based responses.

* HuggingFace Transformers provides access to the llama-3.3-70b-versatile model for text generation.

* sentence-transformers/all-MiniLM-L6-v2 is employed for creating precise document embeddings, ensuring fast and relevant search results.

* FAISS serves as the vector database, optimizing similarity search and document retrieval at scale.

* A custom prompt template guides the model to generate focused, medically accurate answers.

* Robust error handling and a local HuggingFace pipeline fallback ensure uninterrupted functionality even if cloud endpoints fail.

* dotenv manages environment variables securely, including HuggingFace API tokens.

### Impact:
Mediora demonstrates my proficiency in Python, machine learning, and modern AI frameworks, highlighting my ability to design scalable, production-grade AI applications. Hosted on my GitHub, it reflects my dedication to leveraging AI for improving healthcare accessibility and creating intelligent systems that blend reliability, precision, and innovation.


# How to run
### STEPS:

Clone the repository

```bash
git clone https://github.com/Chandan2597/Mediora.git
```

### Step 01 - Create a conda environment after opening the repository

```bash
conda create -n mediora python=3.10 -y
```

```bash
conda activate mediora
```

### STEP 02 - Install the requirements
```bash
pip install -r requirements.txt
```

### Create a `.env` file in the root directory and add your Pinecone & openai credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
GROQ_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


```bash
# run the following command to store embeddings to pinecone
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up localhost:
```


