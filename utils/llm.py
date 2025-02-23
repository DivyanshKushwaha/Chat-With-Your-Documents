import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.8,
    max_tokens=512,
    google_api_key=GOOGLE_API_KEY
)

# Define a structured prompt template
prompt_template = """ 
Context: {context}
Question: {question}

Provide a clear and detailed response based only on the provided context. If the context is empty, respond with "No relevant information available."
Helpful answer: 
"""

prompt = PromptTemplate(template=prompt_template, input_variables=['context', 'question'])

def generate_response(query, context):
    """Generate an LLM response using retrieved document context."""
    formatted_prompt = prompt.format(context=context, question=query)
    response = llm.invoke(formatted_prompt)
    return response.content.strip() if response else "No relevant information available."
