# 📄 Talk to My Resume Chatbot

This is the first project in a series demonstrating modern Generative AI development practices. This application allows recruiters, hiring managers, or anyone interested to chat directly with the content of my resume (or any provided PDF document).

It uses **Context Stuffing**—the simplest form of RAG (Retrieval-Augmented Generation)—to ensure the AI's answers are factually grounded **only** in the provided document, dramatically reducing hallucinations.

## ✨ Key Features

* **Context-Aware Chat:** The AI answers questions strictly based on the content of the `resume.pdf` file.
* **Modern LangChain Architecture:** Built using the latest LangChain 0.2+ modules (`core`, `community`, `openai`) and the expressive **LCEL (LangChain Expression Language)** syntax.
* **Simple Streamlit UI:** A clean, easy-to-use chat interface for immediate interaction.
* **Secure API Management:** Uses a `.env` file to securely load the OpenAI API key.

## 🛠️ Technologies Used

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Framework** | **LangChain** (LCEL) | Orchestrates the entire application flow (Prompt \| Model \| Parser). |
| **Frontend** | **Streamlit** | Creates the interactive, live-updating chat interface. |
| **Model Provider** | `langchain-openai` | Connects the application to powerful LLMs (e.g., GPT-4o-mini). |
| **Data Handling** | `langchain-community` & `pypdf` | Loads and processes the PDF document text. |
| **Environment** | `python-dotenv` | Securely manages environment variables and API keys. |

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

### 1. Project Setup

1.  **Clone or Create the Project Folder:**
    ```bash
    mkdir resume-chatbot
    cd resume-chatbot
    ```
2.  **Create and Activate a Virtual Environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Place Required Files:**
    * Add the `app.py` and `requirements.txt` files to the folder.
    * Place your resume (or any document you want to chat with) in the root folder and name it **`resume.pdf`**.

### 2. Install Dependencies

Install all necessary packages using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt