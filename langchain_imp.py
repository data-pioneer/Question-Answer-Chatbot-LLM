from langchain.llms import GooglePalm
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import Annoy
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import os


from dotenv import load_dotenv
load_dotenv()


# Create Google Palm LLM model
llm = GooglePalm(google_api_key=os.environ["GOOGLE_API_KEY"], temperature=0.1)
# # Initialize instructor embeddings using the Hugging Face model
embedding_function = HuggingFaceInstructEmbeddings()
vectordb_file_path = "Annoy_index"

def createVectorDatabase():
    # Load data from FAQ sheet
    loader = CSVLoader(file_path='health_lifestyle_nutrition_dataset.csv', source_column="prompt", encoding="latin1")
    data = loader.load()

    vector_store_from_docs = Annoy.from_documents(data, embedding_function)
    # Save vector database locally
    vector_store_from_docs.save_local(vectordb_file_path)


def getAnswerChain():
    # Load the vector database from the local folder
    vector_store_from_docs = Annoy.load_local(vectordb_file_path, embedding_function)

    # Create a retriever for querying the vector database
    retriever = vector_store_from_docs.as_retriever(score_threshold = 0.7)

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""


    PROMPT = PromptTemplate(
          template=prompt_template, input_variables=["context", "question"]
    )
    chain_type_kwargs = {"prompt": PROMPT}


    from langchain.chains import RetrievalQA

    chain = RetrievalQA.from_chain_type(llm=llm,
                            chain_type="stuff",
                            retriever=retriever,
                            input_key="query",
                            return_source_documents=False,
                            chain_type_kwargs=chain_type_kwargs)
    return chain

if __name__ == "__main__":
    createVectorDatabase()
    chain = getAnswerChain()
