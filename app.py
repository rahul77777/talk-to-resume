import streamlit as st
import os
from dotenv import load_dotenv

# -----Lanchain Imports-----
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

# 1. Load Environment Variables
load_dotenv()
open_api_key = os.getenv("OPENAI_API_KEY")

if not open_api_key:
    st.error("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
    st.stop()


# 2. Setup Page Config
st.set_page_config(page_title="Talk to My Resume", page_icon="📄")
st.title("📄 Talk to My Resume")
st.markdown("Ask any question about my professional background!")

# 3. Load the Resume (Cached to run only once)
@st.cache_resource
def load_resume_text():
    file_path = "resume.pdf"
    if not os.path.exists(file_path):
        return None
    
    #PyPDFLoader splits the PDF into pages
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    #Combine all pages into a single string
    full_text = "\n".join([doc.page_content for doc in docs])
    return full_text

resume_text = load_resume_text()

if resume_text is None:
    st.error("Resume file not found. Please upload 'resume.pdf' in the application directory.")
    st.stop()

# 4. Initializze the model
llm = ChatOpenAI(model="gpt-5-nano", temperature=0.5)

#5. Define the prompt template
template = """
You are a helpful assistant representing a job candidate. 
Answer questions based ONLY on the following resume context:

<context>
{context}
</context>

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

#6. Create the Chain (LCEL Style)
chain = prompt | llm | StrOutputParser()

#7. Streamlit Chat Interface
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if question := st.chat_input("Ask something (e.g., 'What is your Java Experience?')"):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    # Generate response
    with st.chat_message("assistant"):
        # We invoke the chain with the resume text + user question
        response = chain.invoke({"context": resume_text, "question": question})
        st.markdown(response)
        # Add assistant message to history
        st.session_state.messages.append({"role": "assistant", "content": response})