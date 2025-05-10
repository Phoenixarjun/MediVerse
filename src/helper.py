from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings


#Extract Data From the PDF File
def load_pdf_file(data):
    loader= DirectoryLoader(data,
                            glob="*.pdf",
                            loader_cls=PyPDFLoader)

    documents=loader.load()

    return documents


#Split the Data into Text Chunks
def text_split(extracted_data):
  text_splitter = RecursiveCharacterTextSplitter(
      chunk_size=500,
      chunk_overlap=20,
      length_function=len,
  )
  texts = text_splitter.split_documents(extracted_data)
  return texts


#Download the Embeddings from HuggingFace
def download_huggingface_embeddings():
  embeddings = HuggingFaceEmbeddings(
      model_name="sentence-transformers/all-MiniLM-L6-v2",
  )
  return embeddings