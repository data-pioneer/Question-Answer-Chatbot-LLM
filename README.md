# Question-Answer-Large-Language-Model

# Health Lifestyle Nutrition Q&A: Question and Answer System Based on Google Palm LLM and Langchain for learning purpose  

This is an end to end LLM project based on Google Palm and Langchain. i have build a Q&A system for Health, 
Lifestyle, and Nutrition related question answers.


##  I have used the following libraries for project implementation
  - Langchain + Google Palm: LLM based Q&A
  - Streamlit: UI
  - Huggingface instructor embeddings: Text embeddings
  - Annoy: Vector databse

## Installation

1.Clone this repository to your local machine using:
  git clone https://github.com/data-pioneer/Question-Answer-Large-Language-Model.git

2. Install the required dependencies using pip:
  pip install -r requirements.txt
  pip install google-generativeai
  pip install InstructorEmbedding
  pip3 install sentence-transformers
  pip install annoy


3.Acquire an api key through makersuite.google.com and put it in .env file


  GOOGLE_API_KEY="your_api_key_here"
```
## Usage

1. Run the long chain implementation file by executing:
Python langchain_imp.py 


2. Run the Streamlit app by executing:
streamlit run web_main.py

3.The web app will open in your browser.
- Now you are ready to ask questions. Type your question in Question box and hit Enter

## Sample Questions
  - What are the benefits of  regular exercise?
  - How many glasses of water should you drink per day?
  - What is a balanced diet??

## Project Structure

- web_main.py: The main Streamlit application script.
- langchain_imp.py: This has all the langchain implementation code.
- requirements.txt: A list of required Python packages for the project.
- .env: Configuration file for storing your Google API key.
