
import os
from uuid import uuid4
from operator import itemgetter
from typing import Optional, List, Tuple


from langchain.chat_models import ChatOpenAI
from langchain.memory.chat_message_histories import ZepChatMessageHistory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.prompts.prompt import PromptTemplate
from langchain.schema import AIMessage
from langchain.schema.chat_history import BaseChatMessageHistory
from langchain.schema.runnable.history import RunnableWithMessageHistory
from langchain.vectorstores.zep import CollectionConfig, ZepVectorStore

from langchain_core.runnables import (
    ConfigurableField,
    RunnableBranch,
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
)
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.utils import ConfigurableFieldSingleOption

ZEP_API_URL = os.environ.get("ZEP_API_URL", "http://localhost:8080")

# RAG answer synthesis prompt
template = """Answer the question to the best of your knowledge:
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
    # history_messages_key="chat_history",
    input_messages_key="question"
)