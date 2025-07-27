# Langgraph-FastApi-Streamlit-Chatbot

### Set Up Env

mkdir medical-agent

cd medical-agent

python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate

#### Create a file in Windows
type nul > file.txt

#### Set env variable in Windows
set x=123

type nul > requirements.txt

fastapi
uvicorn
python-dotenv
langgraph
langchain # Downgraded to be compatible with langgraph==0.2.5
langchain_openai
tavily-python
tiktoken
numpy
streamlit
requests

pip install -r requirements.txt

## Test Locally
nohup uvicorn main:app --host 0.0.0.0 --port 80 &

stramlit app.py

curl -X POST "http://<your-ec2-public-ip>/chat" \
     -H "Content-Type: application/json" \
     -d '{"messages": ["What are the symptoms of diabetes?"], "thread_id": "medical_thread_1"}'

https://127.0.0.1:8000/docs         # swagger ui 

