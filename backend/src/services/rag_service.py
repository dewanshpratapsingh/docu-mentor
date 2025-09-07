import os
from langchain_huggingface import (
    HuggingFaceEndpoint,
    HuggingFaceEndpointEmbeddings,
    ChatHuggingFace,   # ✅ use correct one from langchain_huggingface
)
from langchain_community.vectorstores.faiss import FAISS
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

rag_chain = None

def initialize_chain():
    global rag_chain
    print("🚀 Initializing AI chain...")

    hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    if not hf_token:
        raise RuntimeError("❌ Missing HUGGINGFACEHUB_API_TOKEN env variable")

    # Load and split knowledge base
    loader = TextLoader("knowledge.txt")
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = text_splitter.split_documents(docs)

    # Embeddings
    embeddings = HuggingFaceEndpointEmbeddings(
        repo_id="sentence-transformers/all-mpnet-base-v2",
        huggingfacehub_api_token=hf_token,
    )

    vector_store = FAISS.from_documents(split_docs, embeddings)
    retriever = vector_store.as_retriever()

    # LLM (conversational model wrapped for chat-style)
    llm_endpoint = HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        task="conversational",   # ✅ correct task
        temperature=0.7,
        max_new_tokens=512,
        huggingfacehub_api_token=hf_token,
    )
    llm = ChatHuggingFace(llm=llm_endpoint)  # ✅ correct wrapping

    # Prompt
    prompt = ChatPromptTemplate.from_template("""
    Answer the user's question based only on the following context:
    <context>{context}</context>
    Question: {input}
    """)

    document_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, document_chain)

    print("✅ AI chain initialized successfully.")


async def ask_question(question: str) -> str:
    if not rag_chain:
        raise RuntimeError("Chain not initialized.")

    print(f"❓ Processing question: {question}")
    response = await rag_chain.ainvoke({"input": question})

    return response.get("answer", "Sorry, I couldn't find an answer.")