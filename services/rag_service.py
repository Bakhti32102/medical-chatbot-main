"""
MediAssist AI - RAG Chain Service
Provides the retrieval-augmented generation chain for medical Q&A.
"""

from typing import Optional, Tuple, List, Dict, Any

from langchain_classic.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq

from core.prompts import RAG_PROMPT_TEMPLATE
from core.config import RETRIEVAL_K


def create_rag_chain(
    llm: ChatGroq,
    vectorstore: FAISS,
) -> RetrievalQA:
    """Create a RetrievalQA chain for medical question answering.

    Args:
        llm: The Groq LLM instance
        vectorstore: The FAISS vectorstore for retrieval

    Returns:
        Configured RetrievalQA chain
    """
    prompt = PromptTemplate(
        template=RAG_PROMPT_TEMPLATE,
        input_variables=["context", "question"],
    )

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": RETRIEVAL_K},
        ),
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt},
    )

    return chain


def query_medical_knowledge(
    chain: RetrievalQA,
    question: str,
    chat_history: str = "",
) -> Dict[str, Any]:
    """Query the medical knowledge base and return structured results.

    Args:
        chain: The RAG chain
        question: The user's medical question
        chat_history: Optional recent conversation history for context

    Returns:
        Dictionary with 'answer', 'sources', and 'success' keys
    """
    try:
        # Prepend chat history to give the LLM conversational context
        full_question = question
        if chat_history:
            full_question = f"Conversation so far:\n{chat_history}\n\nCurrent question: {question}"

        response = chain.invoke({"query": full_question})

        answer = response.get("result", "")
        raw_sources = response.get("source_documents", [])

        # Extract clean source information
        sources = []
        for doc in raw_sources:
            source_info = {
                "content_preview": doc.page_content[:200] + "..."
                if len(doc.page_content) > 200
                else doc.page_content,
                "metadata": doc.metadata if hasattr(doc, "metadata") else {},
            }

            # Extract document name
            metadata = doc.metadata
            source_info["document"] = metadata.get("source", "Unknown document")

            # Extract page number
            page = metadata.get("page", None)
            source_info["page"] = page

            sources.append(source_info)

        return {
            "answer": answer,
            "sources": sources,
            "success": True,
            "error": None,
        }

    except Exception as e:
        return {
            "answer": "",
            "sources": [],
            "success": False,
            "error": str(e),
        }
