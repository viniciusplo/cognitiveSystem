import logging
from typing import List
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from PyPDF2 import PdfReader

def get_embedding_client(model_name:str=""):
    ## TODO implementar direito
    openai_client = OpenAIEmbeddings(model="text-embedding-ada-002")
    
    return openai_client

def break_document(raw_document, chunk_size = 512, chunk_overlap = 0.0) -> List[Document]:
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        separators = ["\n\n", "\n", "."],
        chunk_size = chunk_size,
        chunk_overlap =chunk_overlap,
        model_name="gpt-4o"
    )
    
    documents = text_splitter.split_documents([Document(page_content=raw_document)])
    
    return documents

def read_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

def read_txt(file):
    text_content = file.read().decode("utf-8")
    return text_content

def get_raw_document(document):
    # Se for um arquivo PDF
    if document.name.endswith('.pdf'):
        pdf_text = read_pdf(document)
        return pdf_text
    
    # Se for um arquivo TXT
    elif document.name.endswith('.txt'):
        text_content = read_txt(document)
        return text_content

