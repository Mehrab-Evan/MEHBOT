
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
import PyPDF2
from langchain.text_splitter import CharacterTextSplitter
from langchain.callbacks import get_openai_callback
import pickle
import db

load_dotenv()
# You MUST add your PDF to local files in this notebook (folder icon on left hand side of screen)

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()

    return text


raw_text = extract_text_from_pdf("Mehrab Evan.pdf")


text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
)
chunks = text_splitter.split_text(raw_text)

from langchain.embeddings import SentenceTransformerEmbeddings

embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
# embeddings = OpenAIEmbeddings()
# embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")

knowledgebase = FAISS.from_texts(texts=chunks, embedding=embeddings)

kb = pickle.dumps(knowledgebase)
db.insert_knowledge(29, kb)
