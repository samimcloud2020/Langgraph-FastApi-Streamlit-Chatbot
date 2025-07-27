# search_tool.py
from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_medical_query(query: str) -> str:
    try:
        response = tavily_client.search(
            query=query,
            search_depth="advanced",
            max_results=5,
            include_domains=["webmd.com", "mayoclinic.org", "nih.gov", "cdc.gov"]
        )
        results = response.get("results", [])
        if not results:
            return "No relevant medical information found."
        summary = "\n".join([f"- {result['title']}: {result['content']}" for result in results])
        return f"Search results:\n{summary}"
    except Exception as e:
        return f"Error during search: {str(e)}"