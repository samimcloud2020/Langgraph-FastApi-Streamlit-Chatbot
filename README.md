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


****************************************************************************************************************
### Import Libraries: 
Import streamlit, requests, json, and uuid for UI, HTTP requests, JSON handling, and unique ID generation.

### Configure Streamlit Page: 
Set page title ("Medical Chatbot"), icon (🏥), and centered layout.
### Initialize Session State:
Create messages list in st.session_state to store conversation history.

Generate unique thread_id using uuid.uuid4() for session tracking.

### Define API Endpoint: 
Set FastAPI URL (http://127.0.0.1:8000/chat) for backend communication.
### Render UI:
Display title and subtitle with a medical disclaimer.

Show conversation history using st.chat_message for user and assistant messages.

### Handle User Input:
Capture user input via st.chat_input.
Append input to messages and display it in a chat bubble.
### Communicate with Backend:
Prepare JSON payload with user input and thread_id.

Send POST request to FastAPI endpoint.

Handle response: extract and display bot response, or show error message if request fails.

### Clear Conversation:
Provide "Clear Conversation" button to reset messages and generate new thread_id.

Refresh app using st.experimental_rerun().

**************************************************************************************************
curl -X POST "http://<your-ec2-public-ip>/chat" \
     -H "Content-Type: application/json" \
     -d '{"messages": ["What are the symptoms of diabetes?"], "thread_id": "medical_thread_1"}'

https://127.0.0.1:8000/docs         # swagger ui 

