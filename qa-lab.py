
import os
from pypdf import PdfReader
import docx  

from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAI

# Load Text to Search

def read_pdf(file_path):
    with open(file_path, "rb") as file:
        pdf_reader = PdfReader(file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

def read_word(file_path):
    doc = docx.Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def read_txt(file_path):
    with open(file_path, "r") as file:
        text = file.read()
    return text

def read_documents_from_directory(directory):
    combined_text = ""
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if filename.endswith(".pdf"):
            combined_text += read_pdf(file_path)
        elif filename.endswith(".docx"):
            combined_text += read_word(file_path)
        elif filename.endswith(".txt"):
            combined_text += read_txt(file_path)
    return combined_text

train_directory = 'docs/'
text = read_documents_from_directory(train_directory)


# Split into chunks
char_text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, 
                                      chunk_overlap=200, length_function=len)
text_chunks = char_text_splitter.split_text(text)
  
# Create embeddings
embeddings = OpenAIEmbeddings()
docsearch = FAISS.from_texts(text_chunks, embeddings)

 # Create a list of questions
queries = [
    "Do emeritus professors have library privileges?", 
    "How many years of service are required to be eligible for emeritus status?", 
    "Who are the main characters in Emma?", 
    "When are Dr. Howard's office hours?", 
    "For Natural Language Processing, what percentage of the final grade are homework assignments?", 
    "When and where does Mobile Application Development meet?"]

# Create a LangChain chain to send queries and related text to OpenAI
llm = OpenAI()
chain = load_qa_chain(llm, chain_type="stuff")

# Answer questions
for query in queries:
    docs = docsearch.similarity_search(query )
    response = chain.invoke({"input_documents" : docs, "question" :query})
    print(" ")
    print(query)
    print(response["output_text"])

# ref: https://youtu.be/Dh0sWMQzNH4e