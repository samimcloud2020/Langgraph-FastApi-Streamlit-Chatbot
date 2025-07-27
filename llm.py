# llm.py
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a medical assistant providing accurate and concise health information. Always clarify that you are not a doctor and recommend consulting a healthcare professional for medical advice. Use search results to provide up-to-date information when available."),
    MessagesPlaceholder("messages")
])

llm_model = prompt_template | llm