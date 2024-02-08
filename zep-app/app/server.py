import os

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.memory.chat_message_histories import ZepChatMessageHistory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema.runnable.history import RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

ZEP_API_URL = os.environ.get("ZEP_API_URL", "http://localhost:8080")


# RAG answer synthesis prompt
template = """Answer the question to the best of your knowledge
If the question cannot be answered using the information provided answer
with "I don't know:
"""
QA_PROMPT = ChatPromptTemplate.from_messages(
    [
        ("system", template),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{question}"),
    ]
)
chain =  QA_PROMPT | ChatOpenAI() | StrOutputParser()

chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: ZepChatMessageHistory(session_id, url=ZEP_API_URL),
    input_messages_key="question",
    history_messages_key="chat_history",
)

app = FastAPI()

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

add_routes(app, chain_with_history)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)